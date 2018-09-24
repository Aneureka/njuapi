import re
import json
import uuid
import base64
import requests
import binascii
from requests.exceptions import ConnectionError
from json.decoder import JSONDecodeError

from app.constants import code, message
from app.utils import build_result


LOGIN_URL = 'http://mids.nju.edu.cn/_ids_mobile/webLogin20_2'
SERVICE_HOST = 'http://mapp.nju.edu.cn/mobile'
BOOK_BORROW_INFO_URL = SERVICE_HOST + '/getBookBorrowInfo.mo'


POST_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}


def login(username, password):
    data = {
        'encoded': 'false',
        'goto': '',
        'gotoOnFail': '',
        'IDToken0': '',
        'loginLT': str(uuid.uuid4()),
        'IDButton': 'Submit',
        'username': str(username),
        'password': str(password),
        'gx_charset': 'UTF-8'
    }

    try:
        resp = requests.post(LOGIN_URL, data=data, headers=POST_HEADERS)
        pattern = re.compile(r'iPortal\.closeWindow\(([^)]+)\)')
        search_result = pattern.findall(resp.text)
        if not search_result:
            return build_result(code=code.INVALID_USERNAME_OR_PASSWORD, err_msg=message.INVALID_USERNAME_OR_PASSWORD)
        login_info = json.loads(search_result[0])
        user_info = _retrieve_user_info(login_info)
        cookie = _retrieve_cookie(login_info)
        token = _encode_cookie(cookie)
        return build_result(user_info=user_info, token=token.decode('utf-8'))

    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def get_book_borrow_info(token):
    try:
        cookie = _decode_token(token)
        raw_info = requests.get(BOOK_BORROW_INFO_URL, cookies=cookie).text
        # TODO handle timeout!!!
        return build_result(book_borrow_info=_retrieve_book_borrow_info(raw_info))
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))
    except binascii.Error:
        return build_result(code=code.INVALID_TOKEN, err_msg=message.INVALID_TOKEN)
    except JSONDecodeError:
        return build_result(code=code.INVALID_TOKEN, err_msg=message.INVALID_TOKEN)


def _retrieve_user_info(login_info):
    return {
        'sid': login_info.get('user').get('data').get('uxid'),
        'name': login_info.get('user').get('data').get('username'),
        'phone': login_info.get('user').get('data').get('mobilePhone'),
        'email': login_info.get('user').get('data').get('email'),
        'gender': login_info.get('user').get('data').get('sex'),
        'department_id': login_info.get('user').get('data').get('departmentId'),
        'dormitory': login_info.get('user').get('data').get('dormitory'),
        'groups': login_info.get('user').get('data').get('groups'),
        'login_info': {
            'cookie_domain': login_info.get('ssoCookie')[0].get('cookieDomain'),
            'i_planet_directory_pro': login_info.get('ssoCookie')[0].get('cookieValue'),
            'user_pwd': login_info.get('userPwd')
        }
    }


def _retrieve_cookie(login_info):
    return {
        'iPlanetDirectoryPro': login_info.get('ssoCookie')[0].get('cookieValue')
    }


def _retrieve_book_borrow_info(raw_info):
    # TODO transform to the format for human
    return raw_info


def _encode_cookie(cookie):
    return base64.b64encode(json.dumps(cookie).encode('utf-8'))


def _decode_token(token):
    try:
        return json.loads(base64.b64decode(token).decode('utf-8'))
    except binascii.Error as e1:
        raise e1
    except JSONDecodeError as e2:
        raise e2


if __name__ == '__main__':
    pass
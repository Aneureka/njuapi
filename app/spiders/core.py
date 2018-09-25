import re
import json
import uuid
import base64
import requests
import binascii
from requests.exceptions import ConnectionError, Timeout
from json.decoder import JSONDecodeError

from app.constants import code, message
from app.utils import build_result

LOGIN_URL = 'http://mids.nju.edu.cn/_ids_mobile/webLogin20_2'
SERVICE_HOST = 'http://mapp.nju.edu.cn/mobile'
BOOK_BORROW_INFO_URL = SERVICE_HOST + '/getBookBorrowInfo.mo'
TRANS_LIST_URL = SERVICE_HOST + '/getTransList.mo'
TEL_BOOK_URL = SERVICE_HOST + '/viewTelBook.mo'

POST_HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}


def core_login(username, password):
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
        print(cookie)
        token = _encode_cookie(cookie)
        return build_result(user_info=user_info, token=token.decode('utf-8'))

    except ConnectionError as e1:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e1))
    except ValueError as e2:
        return build_result(code=code.EMPTY_VALUE, err_msg=str(e2))


def get_book_borrow_info(token):
    try:
        cookie = _decode_token(token)
        raw_info = requests.get(BOOK_BORROW_INFO_URL, cookies=cookie).text
        raw_borrow_info = json.loads(raw_info)
        return build_result(book_borrow_info=_retrieve_book_borrow_info(raw_borrow_info))
    except ConnectionError as e1:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e1))
    except binascii.Error:
        return build_result(code=code.INVALID_TOKEN, err_msg=message.INVALID_TOKEN)
    except JSONDecodeError:
        return build_result(code=code.INVALID_TOKEN, err_msg=message.INVALID_TOKEN)
    except ValueError as e2:
        return build_result(code=code.EMPTY_VALUE, err_msg=str(e2))


def get_trans_list(token):
    try:
        cookie = _decode_token(token)
        raw_info = requests.get(TRANS_LIST_URL, cookies=cookie).text
        raw_trans_list = json.loads(raw_info)
        return build_result(trans_list=_retrieve_trans_list(raw_trans_list))
    except ConnectionError as e1:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e1))


def get_tel_book(department_id=None):
    try:
        data = {'rowCount': 1000}
        if department_id:
            data['id'] = department_id
        raw_info = requests.get(TEL_BOOK_URL, params=data).text
        raw_tel_book = json.loads(raw_info)
        return build_result(tel_book=_retrieve_tel_book(raw_tel_book))
    except ConnectionError as e1:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e1))


def _retrieve_user_info(login_info):
    if login_info:
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
    else:
        raise ValueError('The login information is empty.')


def _retrieve_cookie(login_info):
    if login_info:
        return {
            'iPlanetDirectoryPro': login_info.get('ssoCookie')[0].get('cookieValue')
        }
    else:
        raise ValueError('The login information is empty.')


def _retrieve_book_borrow_info(raw_borrow_info):
    if raw_borrow_info:
        return {
            'accumulation': int(raw_borrow_info.get('data').get('ljjs')),
            'max': int(raw_borrow_info.get('data').get('zdkj')),
            'violation': int(raw_borrow_info.get('data').get('wzcs')),
            'arrears': int(raw_borrow_info.get('data').get('qkje')),
        }
    else:
        raise ValueError('The book borrow information is empty.')


def _retrieve_trans_list(raw_trans_list):
    if raw_trans_list:
        raw_items = raw_trans_list.get('data').get('items')
        items = []
        for item in raw_items:
            items.append({
                'trans_time': item.get('transTime'),
                'trans_name': item.get('transName'),
                'amount': item.get('amount'),
                'balance': item.get('balance'),
                'address': item.get('termName')
            })
        return items
    else:
        raise ValueError('The trans information is empty.')


def _retrieve_tel_book(raw_tel_book):
    if raw_tel_book:
        raw_items = raw_tel_book.get('data').get('items')
        items = []
        for item in raw_items:
            new_item = {'department_id': item.get('id'), 'department_name': item.get('name')}
            if item.get('isChildNode') == 0:
                new_item['phones'] = [x.get('phone') for x in item.get('phones')]
            items.append(new_item)
        return items
    else:
        raise ValueError('The tel book is empty.')


def _encode_cookie(cookie):
    return base64.b64encode(json.dumps(cookie).encode('utf-8'))


def _decode_token(token):
    try:
        return json.loads(base64.b64decode(token).decode('utf-8'))
    except binascii.Error as e1:
        raise e1
    except JSONDecodeError as e2:
        raise e2




import uuid
import re
import json
import requests
from requests.exceptions import ConnectionError

from app.constants import code, message
from app.utils import build_result, build_url

LOGIN_URL = 'http://mids.nju.edu.cn/_ids_mobile/webLogin20_2'

HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}


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
        resp = requests.post(LOGIN_URL, data=data, headers=HEADERS)
        pattern = re.compile(r'iPortal\.closeWindow\(([^)]+)\)')
        search_result = pattern.findall(resp.text)
        if not search_result:
            return build_result(code=code.INVALID_USERNAME_OR_PASSWORD, err_msg=message.INVALID_USERNAME_OR_PASSWORD)
        login_info = _retrieve_login_info(json.loads(search_result[0]))
        return build_result(content=login_info)

    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def _retrieve_login_info(login_info):
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


if __name__ == '__main__':
    pass
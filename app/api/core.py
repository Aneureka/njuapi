from flask import Blueprint, request

from app.spiders.core import *
from app.utils import build_result
from app.constants import code

core = Blueprint('core', __name__)


@core.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')
    return core_login(username, password)


@core.route('/book_borrow_info', methods=['GET'])
def book_borrow_info():
    token = request.args.get('token')
    return get_book_borrow_info(token)


@core.route('/trans_list', methods=['GET'])
def trans_list():
    token = request.args.get('token')
    return get_trans_list(token)


@core.route('/tel_book', methods=['GET'])
def tel_book():
    department_id = request.args.get('department_id')
    return get_tel_book(department_id)


from flask import Blueprint, request

from app.spiders.core import *
from app.utils import build_result
from app.constants import code

core = Blueprint('core', __name__)


@core.route('/login', methods=['POST'])
def login():
    pass
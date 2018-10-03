from flask import Blueprint, request

from app.spiders.bbs import *
from app.utils import build_result
from app.constants import code

bbs = Blueprint('bbs', __name__)


@bbs.route('/sections', methods=['GET'])
def sections():
    return get_sections()


@bbs.route('/boards', methods=['GET'])
def boards():
    return get_board_all()


@bbs.route('/boards/top', methods=['GET'])
def boards_top():
    return get_board_top20()


@bbs.route('/boards/not', methods=['GET'])
def boards_not():
    if 'board' not in request.args:
        return build_result(code=code.INVALID_PARAMS, err_msg='The required param \'board\' is missing.')
    return get_board_not(request.args['board'])


@bbs.route('/articles', methods=['GET'])
def articles():
    if 'board' in request.args:
        if 'pages' in request.args:
            if str.isdigit(request.args['pages']):
                return get_articles_by_board(request.args['board'], int(request.args['pages']))
            else:
                return build_result(code=code.INVALID_NUMBER, err_msg='The param pages is not a number')
        else:
            return get_articles_by_board(request.args['board'])
    elif 'url' in request.args:
        return get_article(request.args['url'])
    else:
        return build_result(code=code.INVALID_PARAMS, err_msg='Invalid params. Either \'board\' and \'pages\'(optional) for articles in board or \'url\' for specific article is required.')


@bbs.route('/articles/hot', methods=['GET'])
def articles_hot():
    return get_hot_topics()


@bbs.route('/articles/top10', methods=['GET'])
def articles_top():
    return get_top10()


@bbs.route('/articles/search', methods=['GET'])
def articles_search():
    args = request.args
    author = args['author'] if 'author' in args else ''
    keyword = args['keyword'] if 'keyword' in args else ''
    days_from_now = args['days'] if 'days' in args else 7
    return search_article(author, keyword, days_from_now)


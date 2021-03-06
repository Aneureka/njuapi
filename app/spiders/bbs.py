import re
import time
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

from app.constants import code, message
from app.utils import build_result, build_url

HOST_URL = 'http://bbs.nju.edu.cn'
TAB_URL = HOST_URL + '/cache_bbsleft.htm'
TOP10_URL = HOST_URL + '/bbstop10'
BOARD_ALL_URL = HOST_URL + '/bbsall'
BOARD_TOP20_URL = HOST_URL + '/bbstopb10'
HOT_TOPICS_URL = HOST_URL + '/bbstopall'
SEARCH_ARTICLE_URL = HOST_URL + '/bbsfind'
BOARD_NOT_URL = HOST_URL + '/bbsnot'
ARTICLE_URL = HOST_URL + '/bbsdoc'

CODE = 'gb2312'


def get_sections():
    try:
        html = requests.get(TAB_URL).text
        soup = BeautifulSoup(html, features='html.parser')
        raw_tabs = soup.find_all('a', attrs={'href': re.compile(r'bbsboa\?sec=\d+')})
        sections = [item.text.strip() for item in raw_tabs]
        return build_result(sections=sections) if sections \
            else build_result(code=code.PARSE_ERROR, err_msg=message.PARSE_HTML_ERROR)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def get_top10():
    pattern = re.compile(
        r'<a href=bbsdoc\?board=\w+>(\w+)</a><td><a href="(\S+)">\s*([^<]+)\s*</a><td><a href=\S+>\s*(\w+)</a><td>(\d+)')
    try:
        html = requests.get(TOP10_URL).text
        top10 = [dict(board=a, url=quote(b), title=c.strip(), author=d, follower=e) for a, b, c, d, e in
                 pattern.findall(html)]
        return build_result(articles=top10) if top10 \
            else build_result(code=code.EMPTY_CONTENT, err_msg=message.EMPTY_CONTENT)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def get_board_top20():
    pattern = re.compile(
        r'<tr><td>(\d+)<td><a href=(bbsdoc\?board=\w+)>(\w+)</a><td width=\d+><a href=bbsdoc\?board=\w+>(\w+)</a><td><a href=bbsqry\?userid=\w+>(\w+)</a><td>(\w+)<td>([\d\.%]+)')
    try:
        html = requests.get(BOARD_TOP20_URL).text
        board_top20 = [dict(seq=a, url=HOST_URL+quote(b), board=c, ch_board=d, moderator=e, cur_online=f, hot=g) for
                       a, b, c, d, e, f, g in pattern.findall(html)]
        return build_result(boards=board_top20) if board_top20 \
            else build_result(code=code.PARSE_ERROR, err_msg=message.PARSE_HTML_ERROR)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def get_board_all():
    pattern = re.compile(
        r'<tr><td>(\d+)<td><a href=([^>]+)>([\dA-Za-z_]+)</a><td>\[(\S+)\]<td><a href=\S+>\s+○\s*(\w+)\s*</a><td>(\S+)</a>')
    try:
        html = requests.get(BOARD_ALL_URL).text
        bbs_all = [dict(seq=a, url=HOST_URL+'/'+b, board=c, type=d, description=e, moderator=f) for a, b, c, d, e, f in
                   pattern.findall(html)]
        return build_result(boards=bbs_all) if bbs_all \
            else build_result(code=code.PARSE_ERROR, err_msg=message.PARSE_HTML_ERROR)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def get_hot_topics():
    pattern = re.compile(r'<td>\S+<a href="(\S+)">([^<]+)</a>\s*\[<a href=bbsdoc\?board=\w+>(\w+)</a>\]')
    try:
        html = requests.get(HOT_TOPICS_URL).text
        bbs_top_all = [dict(url=quote(a), title=b.strip(), board=c) for a, b, c in pattern.findall(html)]
        return build_result(articles=bbs_top_all) if bbs_top_all \
            else build_result(code=code.PARSE_ERROR, err_msg=message.PARSE_HTML_ERROR)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def search_article(author='', keyword='', days_from_now=7):
    data = {
        'flag': 1,
        'user': author,
        'title': keyword,
        'title2': '',
        'title3': '',
        'day': 0,
        'day2': days_from_now
    }

    pattern = re.compile(
        r'<a href=bbsqry\?userid=\w+>(\w+)</a><td width=\d+>([^<]+)<td><a href=([^>]+)>([^<]+)</a>')
    try:
        html = requests.post(SEARCH_ARTICLE_URL, data).text
        if '错误' in html:
            return build_result(code=code.TOO_FREQUENT_ERROR, err_msg=message.TOO_FREQUENT_ERROR)
        articles = [dict(author=a, date=b, url=quote(c), title=d.strip()) for a, b, c, d in pattern.findall(html)]
        return build_result(articles=articles)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def get_board_not(board):
    try:
        html = requests.get(build_url(BOARD_NOT_URL, board=board)).text
        soup = BeautifulSoup(html, features='html.parser')
        raw_not = soup.find('textarea')
        return build_result(board_not=soup.find('textarea').text) if raw_not \
            else build_result(code=code.INVALID_BOARD_NAME, err_msg=message.INVALID_BOARD_NAME)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def get_articles_by_board(board, page=1):
    try:
        articles = _get_articles(build_url(ARTICLE_URL, board=board), page)
        return build_result(articles=articles)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def get_article(url):
    pattern = re.compile(r'发信人: \S+\s+\(([^)]*)\), 信区:\s*([^\n]+)\s*标\s*题:\s+([^\n]+)\s*发信站:[^(]*\(([^)]+)\)\s*([\S\s]*?)\n+\s*(-\n|--\n|【 )')
    try:
        html = requests.get(HOST_URL+'/'+url).text
        soup = BeautifulSoup(html, features='html.parser')
        res = soup.find_all('textarea')
        discussion = []
        for item in res:
            text = item.text.replace('\r\n', '\n')
            find_res = pattern.findall(text)
            if find_res:
                group = find_res[0]
                discussion.append({
                    'author': group[0],
                    'board': group[1],
                    'title': group[2],
                    'created_at': group[3],
                    'content': group[4].replace('\n', '')
                })
        return build_result(discussion=discussion) if res else build_result(code=code.INVALID_POSTFIX, err_msg=message.INVALID_POSTFIX)
    except ConnectionError as e:
        return build_result(code=code.CONNECTION_ERROR, err_msg=str(e))


def _get_articles(url, pages=1):
    pattern = re.compile(
        r'<td><a href=bbsqry\?userid=[^>]+>([^<]+)</a><td><td><nobr>([^<]+)<td><a href=([^>]+)>([^<]+)</a>\(<[^>]+>([\w\.]+)</font>\)<td><font color=\w*>(\d+)</font>')
    try:
        html = requests.get(url).text
        article_list = [dict(author=a, time=b, url=quote(c), title=d.strip(), reply=e, hot=f) for a, b, c, d, e, f in
                        pattern.findall(html)]
        if pages > 1:
            search_result = re.compile(r'<a href=([^>]+)>上一页</a>').findall(html)
            if search_result:
                next_url = search_result[0]
                time.sleep(1)  # avoid connection abortion
                try:
                    article_list.extend(_get_articles(HOST_URL+next_url, pages-1))
                except ConnectionError:
                    pass
        return article_list
    except ConnectionError:
        return []


if __name__ == '__main__':
    print(get_article("http://bbs.nju.edu.cn/bbstcon?board=Girls&file=M.1538052273.A"))
    print(get_article("http://bbs.nju.edu.cn/vd14818/bbstcon?board=V_Suggestions&file=M.1538096272.A"))
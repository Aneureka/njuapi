# -*- coding: utf-8 -*-

"""
提供api
"""

import re
import time

from utils.connect import get_content, post_content
from utils.parse import get_bs_object
from bbs.settings import *


def get_tabs():
	res = get_content(TABS)
	soup = get_bs_object(res)
	raw_tabs = soup.find_all('a', attrs={'href': re.compile(r'bbsboa\?sec=\d+')})
	tabs = list()
	for item in raw_tabs:
		tabs.append(item.text.strip())
	return tabs


def get_top10():
	res = get_content(TOP10)
	pattern = re.compile(r'<a href=bbsdoc\?board=\w+>(\w+)</a><td><a href="(\S+)">\s*(\w+)\s*</a><td><a href=\S+>\s*(\w+)</a><td>(\d+)')
	top10 = [dict(board=a, postfix=b, title=c.strip(), writer=d, follower=e) for a, b, c, d, e in pattern.findall(res)]
	return top10


def get_bbs_board_top20():
	res = get_content(BBS_TOP_B2O)
	pattern = re.compile(r'<tr><td>(\d+)<td><a href=(bbsdoc\?board=\w+)>(\w+)</a><td width=\d+><a href=bbsdoc\?board=\w+>(\w+)</a><td><a href=bbsqry\?userid=\w+>(\w+)</a><td>(\w+)<td>([\d\.%]+)')
	board_top20 = [dict(seq=a, postfix=b, board=c, ch_board=d, moderator=e, cur_online=f, hot=g) for a, b, c, d, e, f, g in pattern.findall(res)]
	print(board_top20)


def get_bbs_all():
	res = get_content(BBS_ALL)
	pattern = re.compile(r'<tr><td>(\d+)<td><a href=(\S+)>([\dA-Za-z_]+)</a><td>\[(\S+)\]<td><a href=\S+>\s+○\s*(\w+)\s*</a><td>(\S+)</a>')
	bbs_all = [dict(seq=a, postfix=b, board=c, type=d, description=e, moderator=f) for a,b,c,d,e,f in pattern.findall(res)]
	return bbs_all


def get_bbs_top_all():
	res = get_content(BBS_TOP_ALL)
	pattern = re.compile(r'<td>\S+<a href="(\S+)">([^<]+)</a>\s*\[<a href=bbsdoc\?board=\w+>(\w+)</a>\]')
	bbs_top_all = [dict(postfix=a, title=b.strip(), board=c) for a, b, c in pattern.findall(res)]
	print(bbs_top_all)


def search_article(user='', title='', title2='', title_without='', from_now_begin=0, from_now_end=7):
	data = {
		'flag': 1,
		'user': str(user).encode(CODE),
		'title': str(title).encode(CODE),
		'title2': str(title2).encode(CODE),
		'title3': str(title_without).encode(CODE),
		'day': str(from_now_begin).encode(CODE),
		'day2': str(from_now_end).encode(CODE)
	}
	res = post_content(SEARCH_ARTICLE, data)
	pattern = re.compile(r'<a href=bbsqry\?userid=\w+>(\w+)</a><td width=\d+>([^<]+)<td><a href=([^>]+)>([^<]+)</a>')
	bbs_find = [dict(writer=a, date=b, postfix=c, title=d.strip()) for a, b, c, d in pattern.findall(res)]
	return bbs_find


def get_bbs_not(board):
	res = get_content(HOST + 'bbsnot?board=' + board)
	soup = get_bs_object(res)
	# TODO: 编码问题
	return soup.find('textarea').text


def get_article_list_by_board(board, page=1, type=0):
	res = get_content(HOST + 'bbsdoc?board=' + board)
	if type == 1:
		pattern = re.compile(r'<tr><td>\d+<td><td><a href=bbsqry\?userid=[^>]+>([^<]+)</a><td>([^<]+)<td><a href=([^>]+)>○\s*([^<]+)</a><td><font color=\w*>(\d+)</font>[^>]+>(\d+)')
		article_list = [dict(writer=a, time=b, postfix=c, title=d.strip(), reply=e, hot=f) for a, b, c, d, e, f in pattern.findall(res)]
	else:
		pattern = re.compile(r'<td><a href=bbsqry\?userid=[^>]+>([^<]+)</a><td><td><nobr>([^<]+)<td><a href=([^>]+)>○\s*([^<]+)</a>\(<[^>]+>([\w\.]+)</font>\)<td><font color=\w*>(\d+)</font>')
		article_list = [dict(writer=a, time=b, postfix=c, title=d.strip(), size=e, hot=f) for a, b, c, d, e, f in pattern.findall(res)]

	while page > 1:
		next_urls = re.compile(r'<a href=([^>]+)>上一页</a>').findall(res)
		if next_urls:
			next_url = next_urls[0]
			res = get_content(HOST + next_url)
			if type == 1:
				article_list.extend([dict(writer=a, time=b, postfix=c, title=d.strip(), reply=e, hot=f) for a, b, c, d, e, f in pattern.findall(res)])
			else:
				article_list.extend([dict(writer=a, time=b, postfix=c, title=d.strip(), size=e, hot=f) for a, b, c, d, e, f in pattern.findall(res)])
			page -= 1
			time.sleep(0.4)
		else:
			break

	return article_list


def get_article(postfix):
	res = get_content(HOST + postfix)
	soup = get_bs_object(res)
	text = soup.find_all('textarea')[0].text
	return text


if __name__ == '__main__':
	print(get_article('bbscon?board=PartTimeJob&file=M.1505481781.A&num=11994'))


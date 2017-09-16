# -*- coding: utf-8 -*-

"""
提供api
"""

import re

from utils.connect import get_content
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
	pattern = re.compile(r'<a href=bbsdoc\?board=[a-zA-Z_]+>([a-zA-Z_]+)</a><td><a href="(\S+)">\s*(\w+)\s*</a><td><a href=\S+>\s*(\w+)</a><td>(\d+)')
	top10 = [dict(board=a, postfix=b, topic=c, writer=d, follower=e) for a, b, c, d, e in pattern.findall(res)]
	return top10


def get_bbs_all():
	res = get_content(BBSALL)
	pattern = re.compile(r'<tr><td>(\d+)<td><a href=(\S+)>([\dA-Za-z_]+)</a><td>\[(\S+)\]<td><a href=\S+>\s+○\s*(\w+)\s*</a><td>(\S+)</a>')
	bbs_all = [dict(seq=a, postfix=b, talk=c, type=d, description=e, moderator=f) for a,b,c,d,e,f in pattern.findall(res)]
	return bbs_all


def get_bbs_top_all():
	pass


def search_article():
	pass




if __name__ == '__main__':
	print(get_top10())

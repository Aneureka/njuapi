# -*- coding: utf-8 -*-

"""
提供api
"""

import re
from bs4 import BeautifulSoup

from settings import *
from njuapi.utils.connect import get_content
from njuapi.utils.parse import get_bs_object

def get_tabs():
	res = get_content(TABS)
	soup = get_bs_object(res)
	raw_tabs = soup.find_all('a', attrs={'href':re.compile(r'bbsboa\?sec=\d+')})
	tabs = list()
	for item in raw_tabs:
		tabs.append(item.text.strip())
	return tabs

def get_top10():
	res = get_content(TOP10)
	pattern = re.compile(r'<a href=bbsdoc\?board=[a-zA-Z_]+>([a-zA-Z_]+)</a><td><a href="(\S+)">(.+)')
	top10 = [dict(board=x, postfix=y, topic=z) for x,y,z in pattern.findall(res)]
	return top10

def get_bbsall():
	res = get_content(BBSALL)
	print(res)

if __name__ == '__main__':
	get_bbsall()
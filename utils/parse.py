# -*- coding: utf-8 -*-

"""
解析网页文本
"""

from bs4 import BeautifulSoup


def get_bs_object(html_doc):
	soup = BeautifulSoup(html_doc, 'lxml')
	return soup

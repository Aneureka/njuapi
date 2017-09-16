# -*- coding: utf-8 -*-

"""
连接器
"""

import requests

from utils.middlewares import get_header

s = requests.Session()

def get(url):
	return s.get(url)


def post(url, data):
	s.get(url)
	return s.post(url, data)


def post_required_cookie(url):
	s.get(url)
	return s.post(url, data)


def get_advanced(s, url):
	return s.get(url)


def post_advanced(s, url, data):
	return s.post(url, data)


def post_content(url, data):
	r = post(url, data)
	return r.text


def get_content(url):
	r = get(url)
	return r.text

def get_jw_content(url):
	r = get(url)
	return r.content

def post_jw_content(url, data):
	r = post(url, data)
	return r.content


def get_session():
	return wrapped(s)


def get_with_cookie(url, cookies):
	return s.get(url=url, cookies=cookies)


def get_cookie(response):
	return response.cookies.get_dict()


def wrapped(s):
	headers = dict()
	headers['User-Agent'] = get_header()
	headers['Content-Type'] = 'text/javascript; charset=utf-8'
	s.headers = headers
	return s


def build_url(host, **args):
	url = host
	if len(args) > 0:
		url += '?'
	arg_list = []
	for key, value in args.items():
		arg_list.append(str(key) + '=' + str(value))
	url += "&".join(arg_list)
	return url

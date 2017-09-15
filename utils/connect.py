# -*- coding: utf-8 -*-

"""
连接器
"""

import requests
from njuapi.utils.middlewares import get_header


def get(url):
	s = get_session()
	return s.get(url)

def post(url, data):
	s = get_session()
	s.get(url)
	return s.post(url, data)

def post_required_cookie(url):
	s = get_session()
	s.get(url)
	return s.post(url, data)

def get_session():
	s = requests.Session()
	return wrapped(s)

def get_with_cookie(url, cookies):
	s = get_session()
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


if __name__ == '__main__':
	url = build_url("https://github.com/login")
	data = {
		'commit': 'Sign in',
		'utf8': '✓',
		'authenticity_token': 'i6PXXJhRVuCwUSMlHFDLUhLkPGJeQkulK2K7ZvC+NlkcQWmyJFQhypZw7jUZQ0JYBH/MMFTtR7MyItxgcD9Twg==',
		'login': 'Aneureka',
		'password': 'guohaobin555'
	}
	rp = post(url, data)
	print(get_cookie(rp))
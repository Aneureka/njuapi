# -*- coding: utf-8 -*-

"""
程序入口
"""

from flask import Flask, request, jsonify

from bbs.api import *

app = Flask(__name__)


# 欢迎
@app.route('/')
def hello_world():
	return '欢迎使用NJU-API，加油~'


# 小百合：所有标签
@app.route('/bbs/get_tabs')
def bbs_get_tabs():
	return jsonify(get_tabs())


# 小百合：十大
@app.route('/bbs/get_top10')
def bbs_get_top10():
	return jsonify(get_top10())


# 小百合：热门讨论区
@app.route('/bbs/get_bbs_board_top20')
def bbs_get_bbs_board_top20():
	return jsonify(get_bbs_board_top20())


# 小百合：全部讨论区
@app.route('/bbs/get_bbs_all')
def bbs_get_bbs_all():
	return jsonify(get_bbs_all())


# 小百合：今日各区热门话题
@app.route('/bbs/get_bbs_top_all')
def bbs_get_bbs_top_all():
	return jsonify(get_bbs_top_all())


# 小百合：进版画面
@app.route('/bbs/get_bbs_not', methods=['GET'])
def bbs_get_bbs_not():
	if request.method == 'GET':
		try:
			board = request.args['board']
			return get_bbs_not(board)
		except:
			return 'param not given!'
	return 'HTTP Method Not GET.'


# 小百合：板块内文章列表
@app.route('/bbs/get_article_list_by_board')
def bbs_get_article_list_by_board():
	if request.method == 'GET':
		try:
			data = request.args.to_dict()
			print(data)
			board = data['board']
			page = int(data.get('page'))
			if page:
				return jsonify(get_article_list_by_board(board, page))
			else:
				return jsonify(get_article_list_by_board(board))
		except:
			return 'param not given!'
	else:
		return 'HTTP Method Not GET.'


# 小百合：搜索文章
@app.route('/bbs/search_article')
def bbs_search_article():
	if request.method == 'POST':
		try:
			return jsonify(search_article(**request.get_data()))
		except:
			return 'param wrong or not given!'
	else:
		return 'HTTP Method Not POST.'


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=666, debug=True)

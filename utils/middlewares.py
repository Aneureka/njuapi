# -*- coding: utf-8 -*-

"""
中间件：获取header等配置
"""

from random import choice
from njuapi.settings import USER_AGENT_CHOICES, DEFAULT_USER_AGENT, rotate_user_agent


def get_header():
	if rotate_user_agent:
		return choice(USER_AGENT_CHOICES)
	else:
		return DEFAULT_USER_AGENT


if __name__ == '__main__':
	print(get_header())

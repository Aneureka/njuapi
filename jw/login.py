import requests
import re
import os
from PIL import Image
import pytesser3

from utils.connect import *
from jw.settings import *

retry_count = 0

# 二值化用
threshold = 140
table = []


def init_table():
	for i in range(256):
		if i < threshold:
			table.append(0)
		else:
			table.append(1)


def load_vcode(path):
	se = requests.Session()
	data = get_byte_content_advanced(se, ValidateURL)
	open(path, 'wb').write(data)
	return se


def twrify(name, save):
	im = Image.open(name)
	# 转化到灰度图
	imgry = im.convert('L')
	# 二值化，采用阈值分割法，threshold为分割点
	out = imgry.point(table, '1')
	region = (1, 1, 79, 19)
	# 裁切黑边
	out = out.crop(region)
	out.save(save)


def get_vcode(language):
	se = load_vcode(PATH)
	twrify(PATH, PATH2)
	s = pytesser3.image_file_to_string(PATH2, language=language)
	num = 4
	result = ''
	for c in s:
		if num == 0:
			break
		elif c == " ":
			pass
		else:
			result += c
			num -= 1
	return [se, result]


def deleteVcode():
	if os.path.exists(PATH):
		os.remove(PATH)
	if os.path.exists(PATH2):
		os.remove(PATH2)


def login(username, password, language):
	try:
		se, vcode = get_vcode(language)
		postData = {'userName': username,
					'password': password,
					'returnUrl': 'null',
					'ValidateCode': vcode
					}
		po = post_byte_content_advanced(se, LoginURL, postData)
		upo = po.decode('utf-8')
		erlist = re.compile('验证码错误')
		ernum = re.findall(erlist, upo)
		global retry_count
		if len(ernum) != 0:
			# 验证码识别出错
			print('验证码错误。将重试。')
			retry_count += 1
			deleteVcode()
			return login(username, password, language)
		else:
			print('登陆成功。重试' + str(retry_count) + "次。")
			retry_count = 0
			deleteVcode()
			return se
	except:
		# 一般是你断网了，或者访问太频繁被教务网封了
		print("未知错误")
		retry_count += 1
		deleteVcode()
		return login(username, password, language)


def Login(username, password):
	init_table()
	return login(username, password, language='fontyp')

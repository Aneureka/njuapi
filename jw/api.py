from jw.login import Login
from jw.settings import *
from utils.connect import *
import re
from requests.exceptions import ConnectionError
from config import connect_error_prompt


# 获取各个学期成绩
# year=年份
# term=学期，填1或2
def getScore(name, password, year, term):
	se = Login(name, password)
	AddScoreURL = ScoreURL + str(year) + str(term)
	try:
		data = get_byte_content_advanced(se, AddScoreURL)
	except ConnectionError:
		return connect_error_prompt
	score = data.decode('UTF-8')
	scorelist = re.compile('middle">(.*?)</td>', re.S)
	scorenum = re.findall(scorelist, score)
	washscore = []
	tmp = []
	for i in range(len(scorenum)):
		if not (i % 9 == 0 or i % 9 == 7 or i % 9 == 8):
			scores = scorenum[i]
			if i % 9 == 1:
				st = scores.find("classid") + 8
				en = scores.find("target") - 2
				Classid = scores[st:en]
				st = scores.find("courseNumber") + 13
				en = scores.find("classid") - 1
				CourseNumber = scores[st:en]
				tmp.append(Classid)
				tmp.append(CourseNumber)
				continue
			if i % 9 == 4:
				scores = scores.replace("\r\n\t\t\t\t\t\t\t\t  \t", "")
				scores = scores.replace("\r\n\t\t\t\t\t\t\t\t  ", "")
			if i % 9 == 6:
				scores = re.findall(r"\d+\.?\d*", scores, re.S)[0]
			tmp.append(scores)
			if i % 9 == 6:
				tmp_dict = dict(zip(score_key, tmp))
				washscore.append(tmp_dict)
				tmp = []
	return washscore


# 获取本学期课程信息
def getLessons(name, password):
	se = Login(name, password)
	try:
		data = get_byte_content_advanced(se, LessonURL)
	except ConnectionError:
		return connect_error_prompt
	lesson = data.decode('UTF-8')
	lessonlist = re.compile('middle">(.*?)</td>', re.S)
	lessonnum = re.findall(lessonlist, lesson)
	washlesson = []
	tmp = []
	for i in range(len(lessonnum)):
		if not (i % 10 == 2 or i % 10 == 7 or i % 10 == 8 or i % 10 == 9):
			lessons = lessonnum[i]
			if i % 10 == 0:
				st = lessons.find("classid") + 8
				en = lessons.find("target") - 2
				lessons = lessons[st:en]
			if i % 10 == 6:
				lessons = lessons.replace("\r\n\t\t\t\t\t  \t", "")
				lessons = lessons.replace("\r\n\t\t\t\t\t  ", "")
				lessons = lessons.replace("<br/>", "|")
			tmp.append(lessons)
			if i % 10 == 6:
				tmp_dict = dict(zip(lesson_key, tmp))
				washlesson.append(tmp_dict)
				tmp = []
	return washlesson


# 获取单门课程详细信息
# CourseNumber和Classid上一步给出
def getCourse(name, password, CourseNumber, Classid):
	se = Login(name, password)
	AddCourseURL = CourseURL + str(CourseNumber) + "&classid=" + str(Classid)
	try:
		data = get_byte_content_advanced(se, AddCourseURL)
	except ConnectionError:
		return connect_error_prompt
	course = data.decode('UTF-8')
	courselist = re.compile('font-weight:bold;padding-bottom:5px">(.*?)：</div>\r\n(.*?)</br></br>', re.S)
	coursenum = re.findall(courselist, course)
	washcourse = course_dict
	washcalendar = []
	tmp = []
	for i in range(len(coursenum)):
		courses = list(coursenum[i])
		courses[1] = courses[1].replace("<br/>", "|")
		courses[1] = re.sub('\|*$', "", courses[1])
		courses[1] = courses[1].replace("\t", "")
		courses[1] = courses[1].replace("\r", "")
		washcourse[course_util_dict[courses[0]]] = courses[1]
	# 周历
	calendarlist = re.compile('padding-right:8px">(.*?)</td>', re.S)
	calendarnum = re.findall(calendarlist, course)[1:]
	for i in range(len(calendarnum)):
		calendars = calendarnum[i]
		calendars = calendars.replace("\n", "")
		calendars = calendars.replace("\r", "")
		tmp.append(calendars)
		if i % 5 == 4:
			tmp_dict = dict(zip(calendar_key, tmp))
			washcalendar.append(tmp_dict)
			tmp = []
	washcourse['TeachingCalendar'] = washcalendar
	return washcourse


if __name__ == "__main__":
	print(getCourse('', '', '25010500', '77486'))

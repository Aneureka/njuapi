from jw.login import Login
from jw.settings import *
from utils.connect import *
import re

#获取各个学期成绩
#year=年份
#term=学期，填1或2
def getScore(year, term):
    se=Login()
    AddScoreURL=ScoreURL+str(year)+str(term)
    data = get_byte_content_advanced(se, AddScoreURL)
    score = data.decode('UTF-8')
    scorelist = re.compile('middle">(.*?)</td>', re.S)
    scorenum = re.findall(scorelist, score)
    washscore=[]
    tmp = []
    for i in range(len(scorenum)):
        if not(i%9==0 or i%9==7 or i%9==8):
            scores=scorenum[i]
            if i%9==1:
                st = scores.find("classid") + 8
                en = scores.find("target") - 2
                Classid = scores[st:en]
                st = scores.find("courseNumber") + 13
                en = scores.find("classid") - 1
                CourseNumber = scores[st:en]
                tmp.append(Classid)
                tmp.append(CourseNumber)
                continue
            if i%9==4:
                scores = scores.replace("\r\n\t\t\t\t\t\t\t\t  \t", "")
                scores = scores.replace("\r\n\t\t\t\t\t\t\t\t  ", "")
            if i%9==6:
                scores=re.findall(r"\d+\.?\d*", scores, re.S)[0]
            tmp.append(scores)
            if i%9==6:
                tmpdict=dict(zip(scorekey, tmp))
                washscore.append(tmpdict)
                tmp=[]
    return washscore

#获取本学期课程信息
def getLessons():
    se=Login()
    data = get_byte_content_advanced(se, LessonURL)
    lesson=data.decode('UTF-8')
    lessonlist = re.compile('middle">(.*?)</td>', re.S)
    lessonnum = re.findall(lessonlist, lesson)
    washlesson=[]
    tmp = []
    for i in range(len(lessonnum)):
        if not(i%10==2 or i%10==7 or i%10==8 or i%10==9):
            lessons=lessonnum[i]
            if i%10==0:
                st=lessons.find("classid")+8
                en=lessons.find("target")-2
                lessons=lessons[st:en]
            if i % 10 == 6:
                lessons=lessons.replace("\r\n\t\t\t\t\t  \t","")
                lessons = lessons.replace("\r\n\t\t\t\t\t  ", "")
                lessons = lessons.replace("<br/>", "|")
            tmp.append(lessons)
            if i%10==6:
                tmpdict=dict(zip(lessonkey, tmp))
                washlesson.append(tmpdict)
                tmp=[]
    return washlesson

if __name__=="__main__":
    print(getScore(2016, 2))

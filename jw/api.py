from jw.login import Login
from jw.settings import *
from utils.connect import *
import re

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
    print(getLessons())

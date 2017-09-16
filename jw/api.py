from jw.login import Login
from jw.settings import *
from utils.connect import *
import re

def getLessons():
    Login()
    data = get_jw_content(LessonURL)
    lesson=data.decode('UTF-8')
    lessonlist = re.compile('middle">(.*?)</td>')
    lessonnum = re.findall(lessonlist, lesson)
    print(lessonnum)

if __name__=="__main__":
    getLessons()

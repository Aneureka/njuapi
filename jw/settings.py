#验证码临时路径，可以自己填
PATH='F:/1.jpg'

#验证码二值化临时路径，也可以自己填
PATH2='F:/2.jpg'

#学号自己填
NAME=''

#密码自己填
PASSWORD=''

ValidateURL="http://elite.nju.edu.cn/jiaowu/ValidateCode.jsp"

LoginURL="http://elite.nju.edu.cn/jiaowu/login.do"

LessonURL="http://elite.nju.edu.cn/jiaowu/student/teachinginfo/courseList.do?method=currentTermCourse"

ScoreURL="http://elite.nju.edu.cn/jiaowu/student/studentinfo/achievementinfo.do?method=searchTermList&termCode="

CourseURL="http://elite.nju.edu.cn/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber="

lessonkey=['Classid', 'CourseNumber', 'CourseName', 'District', 'Teacher', 'TimeandPlace']

scorekey=['Classid', 'CourseNumber', 'CourseName', 'EnCourseName', 'CourseType', 'Credit', 'Score']

calendarkey=['Week', 'TeachingContent', 'Teacher', 'TeachingMethod', 'Remark']

coursedict={'CourseName':'','EnCourseName':'','Prerequisite':'','CourseBookProposal':'','ReferenceMaterial':'','TeachingContent':'','EnIntroduction':'','TeachingAim':'','OtherRequirement':'','TeachingCalendar':''}

courseutildict={'教学目标': 'TeachingAim', '参考资料': 'ReferenceMaterial', '其它要求': 'OtherRequirement', '课程名': 'CourseName', '英文名': 'EnCourseName', '建议教材': 'CourseBookProposal', '先修课程': 'Prerequisite', '英文简介': 'EnIntroduction', '教学内容': 'TeachingContent'}
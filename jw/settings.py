# 验证码临时路径，可以自己填
PATH='F:/1.jpg'

# 验证码二值化临时路径，也可以自己填
PATH2='F:/2.jpg'

HOST = "http://elite.nju.edu.cn/"

JW_HOST = HOST + "jiaowu/"

ValidateURL = HOST + "ValidateCode.jsp"

LoginURL = JW_HOST + "login.do"

LessonURL = JW_HOST + "student/teachinginfo/courseList.do?method=currentTermCourse"

ScoreURL = JW_HOST + "student/studentinfo/achievementinfo.do?method=searchTermList&termCode="

CourseURL = JW_HOST + "student/elective/courseList.do?method=getCourseInfoM&courseNumber="

lesson_key=['Classid', 'CourseNumber', 'CourseName', 'District', 'Teacher', 'TimeandPlace']

score_key=['Classid', 'CourseNumber', 'CourseName', 'EnCourseName', 'CourseType', 'Credit', 'Score']

calendar_key=['Week', 'TeachingContent', 'Teacher', 'TeachingMethod', 'Remark']

course_dict={'CourseName':'','EnCourseName':'','Prerequisite':'','CourseBookProposal':'','ReferenceMaterial':'','TeachingContent':'','EnIntroduction':'','TeachingAim':'','OtherRequirement':'','TeachingCalendar':''}

course_util_dict={'教学目标': 'TeachingAim', '参考资料': 'ReferenceMaterial', '其它要求': 'OtherRequirement', '课程名': 'CourseName', '英文名': 'EnCourseName', '建议教材': 'CourseBookProposal', '先修课程': 'Prerequisite', '英文简介': 'EnIntroduction', '教学内容': 'TeachingContent'}
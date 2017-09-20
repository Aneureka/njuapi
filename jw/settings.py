# 验证码临时路径，可以自己填
PATH='F:/1.jpg'

# 验证码二值化临时路径，也可以自己填
PATH2='F:/2.jpg'

# DEBUG开关
DEBUG=True

login_error_prompt_null_nameorpasswd = {'error_code': 1, 'prompt': '用户名或密码为空'}

login_error_prompt_wrong_nameorpasswd = {'error_code': 1, 'prompt': '用户名或密码错误'}

login_error_prompt_wrong_timeout = {'error_code': 1, 'prompt': '重试次数过多'}

MAX_RETRY_COUNT=15

HOST = "http://elite.nju.edu.cn/jiaowu/"

ValidateURL = HOST + "ValidateCode.jsp"

LoginURL = HOST + "login.do"

LessonURL = HOST + "student/teachinginfo/courseList.do?method=currentTermCourse"

ScoreURL = HOST + "student/studentinfo/achievementinfo.do?method=searchTermList&termCode="

CourseURL = HOST + "student/elective/courseList.do?method=getCourseInfoM&courseNumber="

lesson_key=['Classid', 'CourseNumber', 'CourseName', 'District', 'Teacher', 'TimeandPlace']

score_key=['Classid', 'CourseNumber', 'CourseName', 'EnCourseName', 'CourseType', 'Credit', 'Score']

calendar_key=['Week', 'TeachingContent', 'Teacher', 'TeachingMethod', 'Remark']

course_dict={'CourseName':'','EnCourseName':'','Prerequisite':'','CourseBookProposal':'','ReferenceMaterial':'','TeachingContent':'','EnIntroduction':'','TeachingAim':'','OtherRequirement':'','TeachingCalendar':''}

course_util_dict={'教学目标': 'TeachingAim', '参考资料': 'ReferenceMaterial', '其它要求': 'OtherRequirement', '课程名': 'CourseName', '英文名': 'EnCourseName', '建议教材': 'CourseBookProposal', '先修课程': 'Prerequisite', '英文简介': 'EnIntroduction', '教学内容': 'TeachingContent'}
import re
import datetime
from config import Year
import json


"""
解析课表并返回所有数据
"""
def StudentsInformation(soup):
    # 正则
    findCourseName = re.compile(r'<b class="fontcourse">.*?[(](.*?)[)].*</b>', re.S)  # 课程缩写
    findCourseNames = re.compile(r'<b class="fontcourse">.*?[)](.*?)[(].*</b>', re.S)  # 课程全称
    findTeacher  = re.compile(r'</b>.*?[(].*["师"][\[](.*)["室"].*[)].*<br/></td>', re.S)


    Scname_name = []  # 课程缩写与全称对应表

    # course_number = 1

    for item in soup.select('.detail'):
        if item.get_text().strip() != '':
            # for item2 in soup.find_all('b', class_="fontcourse"):
            temp = []
            item = str(item)


            CourseName = re.findall(findCourseName, item)[0].strip()  # 课程缩写
            CourseNames = re.findall(findCourseNames, item)[0].strip()  # 课程全称
            TeacherName = re.findall(findTeacher,item)[0].replace("]","") #教师名字


            temp.append(CourseName)
            temp.append(CourseNames)
            temp.append(TeacherName)
            # temp.append(course_number)
            # course_number += 1
            Scname_name.append(temp)

    # print(Scname_name)



    #创造总周数字典
    findInitalDate = re.compile(r'.*["01周"]*<br/>(.*)-.*</td>',re.S)
    findendDate =  re.compile(r'.*["01周"]*<br/>.*-(.*)</td>',re.S)
    week_dict ={}
    week_count = 1
    for w in soup.select('.td1'):
        w = str(w)
        initalWeekDate = re.findall(findInitalDate,w)
        endWeekDate = re.findall(findendDate,w)

        if initalWeekDate != []:
            initalWeekDate = str(Year) + "-" + initalWeekDate[0].replace("/", "-")
            endWeekDate = str(Year) + "-" + endWeekDate[0].replace("/", "-")
            # initalWeekDate = datetime.datetime.strptime(initalWeekDate,'%Y-%m-%d')
            # endWeekDate = datetime.datetime.strptime(endWeekDate,'%Y-%m-%d')
            Wkey = initalWeekDate + "~" + endWeekDate
            if week_count< 10:
                value = "0{n}周".format(n=week_count)
                week_count += 1
            else:
                value = "{n}周".format(n=week_count)
                week_count += 1
            week_dict[Wkey] = value

    #初始01周的日期获取
    findMonth = re.compile(r'(.*)[/]')
    findDay = re.compile(r'.*[/](.*)')
    for w in soup.select('.td1'):
        w = str(w)
        initalWeekDate1 = re.findall(findInitalDate,w)
        if initalWeekDate1 != []:
            month = re.findall(findMonth,initalWeekDate1[0])
            day  = re.findall(findDay,initalWeekDate1[0])
            break

    Month = int(month[0])
    Day = int(day[0])

    InitialDate = datetime.date(Year, Month, Day)
    formatDate = InitialDate.strftime('%Y-%m-%d')

    # for item2 in soup.select('.detail'):
    #     if item2.get_text().strip() != '':
    #         item2 = str(item2)
    #         # print(item2)
    #         TeacherName = re.findall(findTeacher,item2)[0].replace("]","")
    #         print(TeacherName)

    findName = re.compile(r'["学号:"]*[\d]*["姓"]["名"][":"](.*)["班"].*', re.S)
    for s in soup.select('.title1'):
        if s.get_text().strip() != '':
            s = str(s.get_text())
            StudentName = re.findall(findName,s)[0].strip()


    # course_count = 0  # 课数计数

    count = 0  # 课时计数
    day_count = 1 #周数计数
    week_day = 1 #第几周
    all_data = []
    course_data = []
    for item in soup.select('.fontcss'):
        if item.get_text().strip() != '':
            course = item.get_text()

            Teacher = '' #老师
            ctime = item.get("colspan", "1") #课时时长
            count = count + int(ctime)       #
            timee = CourseDate(count, ctime)
            start_time = CourseTime(count, ctime)
            # cdut_week = get_week(formatDate, Month)
            my_dict = {}
            # course_count += 1
            # 课程日期
            # courseDate = str(formatDate)
            # 课时
            day_time = str(ctime)


            for key in Scname_name:
                if key[0] in course:
                    course = key[1]
                    Teacher = key[2]
                    # course_n = key[3]
                #     if week_day not in key:
                #         key.append(week_day)
                # print(key)

            # 课程名
            #
            # print(week_data)

            try:
                cplace = item.font.string
            except AttributeError as e:
                cplace = ''

            curriculum = course  # 课程名
            # 地点
            location = cplace
            # 开始时间
            startTime = timee[0]
            # 结束时间
            endTime = timee[1]
            # 开始课节
            start_Section = start_time[0]
            # 结束课时
            end_Section = int(start_Section) + int(day_time) - 1
            # 获取星期几
            day = get_weekDay(formatDate)

            #添加数据
            if curriculum != '教研' and  curriculum != '报到注册' and  curriculum != '考试周' and  curriculum !='研究生考试'\
                    and curriculum !='全国英语四六级' and curriculum !='不排课' and curriculum !='艺考' and '节' not in curriculum\
                    and curriculum != '全国计算机等级考试':

                my_dict['name'] = curriculum #课程名
                my_dict['teacher'] = Teacher #老师
                my_dict['room'] = location #地点
                my_dict['days'] = str(day) #星期几
                my_dict['nums'] = str(start_Section) #开始课时
                my_dict['enums'] = str(end_Section) #结束课时
                my_dict['Week'] = str(week_day) #第几周
                # my_dict['Course_n'] = str(course_n) #课程编号
                # my_dict['Date'] = str(courseDate)
                # my_dict['Class_hour'] = str(day_time)

                # my_dict['StartTime'] = str(startTime)
                # my_dict['EndTime'] = str(endTime)
                all_data.append(my_dict)
                # print(count, '课程:', course, '时长:', ctime, '地点:', cplace, '时间:', timee,'课数:',course_count)
                # print(day_count)
        else:
            # print('2-没课')
            count = count + 1

        # 1天过去了
        if count == 12:
            count = 0
            day_count += 1
            InitialDate = getDate(InitialDate, 1)  # 日期加一
            formatDate = str(InitialDate.strftime('%Y-%m-%d'))  # 化为日历文件日期标准格式

        if day_count == 7:
            day_count = 0
            week_day += 1

        # print(day_count)
        # print(week_day)
    # print(all_data)
    return all_data,StudentName

#获取星期几
def get_weekDay(formatDate):
    year = int(datetime.datetime.strptime(formatDate, '%Y-%m-%d').strftime('%Y'))
    month = int(datetime.datetime.strptime(formatDate, '%Y-%m-%d').strftime('%m'))
    day = int(datetime.datetime.strptime(formatDate, '%Y-%m-%d').strftime('%d'))

    week_day = datetime.datetime(year,month,day).isoweekday()
    return week_day



# def get_week(formatDate,Initialmonth):
#     #获取课程日期信息
#     year = int(datetime.datetime.strptime(formatDate, '%Y-%m-%d').strftime('%Y'))
#     month = int(datetime.datetime.strptime(formatDate, '%Y-%m-%d').strftime('%m'))
#     day = int(datetime.datetime.strptime(formatDate, '%Y-%m-%d').strftime('%d'))
#
#     # 获取第几周
#     if year == Year:
#             week_get = datetime.date(year, month, day).isocalendar()[1]
#     elif year == (Year + 1):
#             week_get = datetime.date(year, month, day).isocalendar()[1]
#
#     if 8 <= Initialmonth < 12:
#         if week_get >= 35:
#             cdut_week = week_get - 34
#         else:
#             cdut_week = week_get + 18
#     elif 3 <= Initialmonth <= 7 :
#             cdut_week = week_get - 8
#
#
#     return cdut_week



# 课程时间字典
def CourseDate(count, ctime):
    key = str(count) + '-' + str(ctime)
    CourseDateKey = {
                     '1-1':['8:10','8:55'],
                     '2-2':['8:10','9:45'],'2-1':['9:00','9:45'],
                     '3-1':['10:15','11:00'],'3-2':['9:45','11:00'], '3-3':['8:10','11:00'],
                     '4-2':['10:15','11:50'], '4-4': ['8:10','11:50'], '4-1':['11:05','11:50'], '4-3':['9:00','11:50'],
                     '5-5':['8:10','14:30'],'5-1':['11:50','14:30'],'5-2':['10:15','14:30'],'5-4':['9:00','14:30'],'5-3':['11:05','14:30'],
                     '6-1':['14:30','15:15'],'6-2':['11:50','15:15'],'6-3':['11:05','15:15'],'6-4':['10:15','15:15'],'6-5':['9:00','15:15'],'6-6':['8:10','15:15'],
                     '7-2':['14:30','16:05'], '7-1':['15:20','16:05'],'7-3':['11:50','16:05'],'7-4':['11:05','16:05'],'7-5':['10:15','16:05'],'7-6':['9:00','16:05'],'7-7':['8:10','16:05'],
                     '8-1':['16:25','17:10'],'8-2':['15:20','17:10'],'8-3':['14:30','17:10'],'8-4':['11:50','17:10'],
                     '8-5': ['11:05', '17:10'],'8-6':['10:15','17:10'],'8-7':['9:00','17:10'],'8-8':['8:10','17:10'],
                     '9-2':['16:25','18:00'],'9-3':['15:20','18:00'], '9-4': ['14:30','18:00'], '9-9': ['8:10','18:00'],'9-1':['17:15','18:00'],
                     '9-5': ['11:50', '18:00'],'9-6':['11:05','18:00'],'9-7':['10:15','18:00'],'9-8':['9:00','18:00'],
                     '10-1':['19:10','19:55'],'10-2':['17:15','19:55'],'10-3':['16:25','19:55'],'10-4':['15:20','19:55'],'10-5':['14:30','19:55'],
                     '10-6': ['11:50', '19:55'],'10-7':['11:05','19:55'],'10-8':['10:15','19:55'],'10-9':['9:00','19:55'],'10-10':['8:10','19:55'],
                     '11-1':['20:00','20:45'],'11-2':['19:10','20:45'],'11-3':['17:15','20:45'],'11-4':['16:25','20:45'],'11-5':['15:20','20:45'], '11-6': ['14:30','20:45'],
                     '11-7': ['11:50', '20:45'],'11-8':['11:05','20:45'],'11-9':['10:15','20:45'],'11-10':['9:00','20:45'],'11-11':['8:10','20:45'],
                     '12-1': ['20:50','21:35'],'12-2': ['20:00','21:35'],
                     '12-3':['19:10','21:35'], '12-4': ['17:15','21:35'],'12-5': ['16:25','21:35'], '12-6': ['15:20','21:35'],'12-7': ['14:30','21:35'],'12-8':['11:50','21:35'],
                     '12-9': ['11:05','21:35'],'12-10': ['10:15','21:35'],'12-11':['9:00','21:35'],
                     '12-12':['8:10','21:35']
    }
    if CourseDateKey.__contains__(key):
        return CourseDateKey[key]
    else:
        print('错误', key)
        return 434


# 课程作息时间
def CourseTime(count, ctime):
    key = str(count) + '-' + str(ctime)
    CourseDateKey = {
                     '1-1':['1'],
                     '2-2':['1'],'2-1':['2'],
                     '3-1':['3'],'3-2':['2'], '3-3':['1'],
                     '4-2':['3'], '4-4': ['1'], '4-1':['4'], '4-3':['2'],
                     '5-5':['1'],'5-1':['5'],'5-2':['4'],'5-3':['3'],'5-4':['2'],
                     '6-1':['6'],'6-2':['5'],'6-3':['4'],'6-4':['3'],'6-5':['2'],'6-6':['1'],
                     '7-2':['6'], '7-1':['7'],'7-3':['5'],'7-4':['4'],'7-5':['3'],'7-6':['2'],'7-7':['1'],
                     '8-1':['8'],'8-2':['7'],'8-3':['6'],'8-4':['5'],'8-5':['4'],'8-6':['3'],'8-7':['2'],'8-8':['1'],
                     '9-2':['8'],'9-3':['7'], '9-4': ['6'], '9-9': ['1'],'9-5':['5'],'9-6':['4'],'9-7':['3'],'9-8':['2'],'9-1':['9'],
                     '10-1':['10'],'10-2':['9'],'10-3':['8'],'10-4':['7'],'10-5':['6'],
                     '10-6': ['5'],'10-7':['4'],'10-8':['3'],'10-9':['2'],'10-10':['1'],
                     '11-2':['10'], '11-6': ['6'],'11-1':['11'],'11-3':['9'],'11-4':['8'],'11-5':['7'],
                     '11-7': ['5'],'11-8':['4'],'11-9':['3'],'11-10':['2'],'11-11':['1'],
                     '12-1':['12'],'12-2':['11'],
                     '12-3':['9'], '12-4':['9'],'12-5': ['8'], '12-6':['7'],'12-7': ['6'],'12-8':['5'],
                     '12-9':['4'],'12-10':['3'],'12-11':['2'],
                     '12-12':['1']
    }
    if CourseDateKey.__contains__(key):
        return CourseDateKey[key]
    else:
        print('错误', key)
        return 434



# InitialDate数据类型实例-datetime.date(2020, 8, 31)
def getDate(InitialDate, changeDays):
    delta = datetime.timedelta(days=changeDays)
    newDate = InitialDate + delta
    # print(newDate)
    return newDate



def schedule_json_data(data,code):
    all_data = {
            'code':str(code),
            'numberOfWeek':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            'data':data
        }
    return json.dumps(all_data,ensure_ascii=False,)


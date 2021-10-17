from config import *
from bs4 import BeautifulSoup
from Schedule import StudentsInformation
from DealData import DealData
Inform_dict = {}

if __name__ == '__main__':
    # html,code = user_schedule(username,password,login_link,schedule_link)
    #
    # with open("2.html",'w',encoding='utf-8') as file:
    #     file.write(html)

    f = open("2.html",'r',encoding='utf-8')
    html = f.read()
    soup = BeautifulSoup(html,"lxml")
    data,student_name = StudentsInformation(soup)
    if data != []:
        courseData = DealData(data)
        Inform_dict['student'] = student_name
        Inform_dict['xuehao'] = username
        Inform_dict['password '] = password
        Inform_dict['course'] = courseData
        print(Inform_dict)
    else:
        Inform_dict['student'] = student_name
        Inform_dict['xuehao'] = username
        Inform_dict['password '] = password
        Inform_dict['course'] = data
        print(Inform_dict)
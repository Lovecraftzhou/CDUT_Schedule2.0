from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from Schedule import StudentsInformation
from DealData import DealData
Inform_dict = {}

browser = webdriver.Firefox()
browser.get('http://jwxtxs.cdut.edu.cn:805/Login.html')
wait = WebDriverWait(browser, 10)
input_count = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[1]/div[1]/span[1]/input')))
input_count.send_keys('201813160220')
input_password = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/form/div/div[1]/div[1]/span[2]/input')))
input_password.send_keys('510421200002042918')
submit = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div/div[1]/div[2]/input')))
submit.click()
submit = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[4]/div[1]/ul/li[4]/a/span')))
submit.click()

year = ["2021","2020","2019","2018"]
faculty = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19"]
major = ["01","02","03","04","05","06","07","08","09","10","11","12","13"]
grade = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]
number = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"]


if __name__ == '__main__':
    for yea in year:
        for fac in faculty:
            for maj in major:
               for gra in grade:
                    for num in number:
                        url = 'http://jwxtxs.cdut.edu.cn:805/Classroom/ProductionSchedule/StuProductionSchedule.aspx?termid=202101&stuID='+yea+fac+maj+gra+num
                        browser.get(url)
                        name = browser.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td')
                        if name.text != '':
                            html = browser.page_source
                            soup = BeautifulSoup(html,"lxml")
                            try:
                                data,student_name = StudentsInformation(soup)
                                courseData = DealData(data)
                                Inform_dict['student'] = student_name
                                Inform_dict['xuehao'] = yea+fac+maj+gra+num
                                Inform_dict['password '] = ''
                                Inform_dict['course'] = courseData
                                txt_path = "E:\\pythonProject\\gooy\\kebiao_txt\\course_data_" + yea + fac + maj + '.txt'
                                with open(txt_path, 'a', encoding='utf8') as f:
                                    f.write(str(Inform_dict))
                                    f.write(',')
                            except:
                                name = name.text.split(' ')
                                xuehao = name[0].split(':')[1]
                                xinming = name[1].split(':')[1]
                                course_data = {"student": xinming,
                                               "xuehao": xuehao,
                                               "password": '',
                                               'course':''}
                                course_data = str(course_data)+','
                                txt_path = "E:\\pythonProject\\gooy\\kebiao_txt\\course_data_" + yea + fac + maj + '.txt'
                                with open(txt_path, 'a', encoding='utf8') as f:
                                    f.write(str(course_data))
                                    f.write(',')
                        else:
                            break

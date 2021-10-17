import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from config import sleep_time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


"""
模拟登录获取课表网页
"""
def user_schedule(username,password,badidu_link,schedule_link):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)  # 禁止下载图片，根据情况使用
    # 禁用浏览器缓存
    profile.set_preference("network.http.use-cache", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.sessionhistory.max_total_viewers", 3)
    profile.set_preference("network.dns.disableIPv6", True)
    profile.set_preference("Content.notify.interval", 750000)
    profile.set_preference("content.notify.backoffcount", 3)
    LOGGER.setLevel(logging.FATAL)
    browser_options = Options()
    # 设置后台运行,不弹出
    # browser_options.add_argument('--headless')
    # browser_options.add_argument('--disable-gpu')
    # browser_options.add_argument("disable-cache")  # 禁用缓存
    # browser_options.add_argument('log-level=4') #关闭日志,禁止打印日志
    driver = webdriver.Firefox(options = browser_options)
    wait = WebDriverWait(driver, 10, 0.5)

    try:
        #连接到百度
        driver.get(url=badidu_link)
        #获取百度中成都理工大学学生登录网站


        # href = driver.find_element_by_partial_link_text("学生登陆")
        href = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[3]/div/div[1]/div/dl/dd/a[1]')))
        link = href.get_attribute("href")
        #跳转到成都理工大学学生登录网站
        driver.execute_script("window.open('"+link+"')")
        driver.switch_to.window(driver.window_handles[1])
    except:
        driver.quit()
        return 434

    time.sleep(1)

    try:
        # account = driver.find_element_by_css_selector("#txtUser")
        # pwd = driver.find_element_by_css_selector("#txtPWD")
        # submit = driver.find_element_by_css_selector("#ibtnLogin")
        account = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#txtUser")))
        pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#txtPWD")))
        submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ibtnLogin")))
    except:
        driver.quit()
        return 434

    account.send_keys(username)
    pwd.send_keys(password)
    submit.click()
    time.sleep(sleep_time)

    #跳转到课表并获取页面源码
    schedule_link = schedule_link
    driver.execute_script("window.open('"+schedule_link+"')")
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(2)
    course_html = driver.page_source
    time.sleep(sleep_time)
    #获取html之后关闭页面
    driver.quit()
    return course_html,200

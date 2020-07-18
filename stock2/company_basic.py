from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


cninfo = 'http://webapi.cninfo.com.cn/#/company?companyid=000001'


# 打开浏览器
driver = webdriver.Chrome(executable_path='/Users/leewow/run/mine/迈克数据/数据爬取/chromedriver')
# 打开亚马逊主页
driver.get(cninfo)

time.sleep(10)

def get_ele2(driver, xpath, msg):
    element = driver.find_element_by_xpath(xpath)
    count = 1
    while not element.is_enabled():
        time.sleep(1)
        element = driver.find_element_by_xpath(xpath)
        count = count + 1
        if count == 3:
            print(msg + ' 获取三次都是fail啦！')
            break
        return element

def get_ele(driver, xpath, msg):
    try:
        print("YOU link found and returned," + msg)
        (WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))))
        return driver.find_element_by_xpath(xpath)

    except TimeoutException:
        print("YOU link not found ... breaking out")


ele = get_ele(driver,'/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/ul/li[2]','公司概况')
time.sleep(3)
ele.click()


# basic_info_btn = get_ele(driver, '/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[1]/ul[1]/li[1]/a','基本信息1') # 基本信息
# time.sleep(10)
# basic_info_btn.click()

basic_info_btn2 = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/a','基本信息2') # 基本信息
time.sleep(3)
basic_info_btn2.click()

# basic_shangshi_btn = get_ele(driver, '/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[1]/ul[1]/li[2]/a','上市1') # 基本信息
# time.sleep(10)
# basic_shangshi_btn.click()

basic_shangshi_btn2 = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[2]/div/div[1]/div/a','上市2') # 基本信息
time.sleep(3)
basic_shangshi_btn2.click()


# basic_ceo_btn = get_ele(driver, '/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/div/div[1]/ul[1]/li[3]/a','高管1') # 基本信息
# time.sleep(10)
# basic_ceo_btn.click()

basic_ceo_btn2 = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[3]/div/div[1]/div/a','高管2') # 基本信息
time.sleep(3)
basic_ceo_btn2.click()





driver.close()



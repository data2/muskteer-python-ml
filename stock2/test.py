import pickle
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

session_file = 'browser_session.data'


def create_driver():
    driver = webdriver.Chrome(executable_path='/Users/leewow/run/mine/迈克数据/数据爬取/chromedriver')
    with open(session_file, 'wb') as f:
        params = {"session_id": driver.session_id, "server_url": driver.command_executor._url}
        pickle.dump(params, f)

    return driver


def get_ele(driver, xpath, msg):
    try:
        (WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))))
        return driver.find_element_by_xpath(xpath)
    except Exception:
        print("YOU link not found ... breaking out" + msg)

def dealOnePage(driver, id):
    try:
        driver.get('http://webapi.cninfo.com.cn/#/company?companyid=000001'+id)

        time.sleep(10)

        #
        ele = get_ele(driver, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/ul/li[2]', '公司概况')
        time.sleep(3)
        ele.click()

        #
        basic_info_btn2 = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/a',
                                  '基本信息')  # 基本信息
        time.sleep(3)
        basic_info_btn2.click()

        #
        basic_shangshi_btn2 = get_ele(driver,
                                      '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[2]/div/div[1]/div/a',
                                      '上市')  # 基本信息
        time.sleep(3)
        basic_shangshi_btn2.click()

        #
        basic_ceo_btn2 = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[3]/div/div[1]/div/a',
                                 '高管')  # 基本信息
        time.sleep(3)
        basic_ceo_btn2.click()



        #####################

        ele = get_ele(driver, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[1]/ul/li[7]/a', '财务数据')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[1]/ul/li[2]/a', '主要财务指标年报')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[1]/div[2]/a', '下载')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[1]/ul/li[3]/a', '主要财务指标中报')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[1]/div[2]/a', '下载')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[1]/ul/li[4]', '主要财务指标一季报')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[1]/div[2]/a', '下载')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[1]/ul/li[5]/a', '主要财务指标三季报')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[1]/div[2]/a', '下载')
        time.sleep(3)
        ele.click()


        ###
        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[3]/ul/li[2]/a', '利润表年报')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[3]/div[1]/div/a', '下载')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[3]/ul/li[3]/a', '利润表中报')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[3]/div[1]/div/a', '下载')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[3]/ul/li[4]/a', '利润表一季报')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[3]/div[1]/div/a', '下载')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[3]/ul/li[5]/a', '利润表三季报')
        time.sleep(3)
        ele.click()

        #
        ele = get_ele(driver, '/html/body/div[1]/div[3]/div/div/div/div/div[7]/div[3]/div[1]/div/a', '下载')
        time.sleep(3)
        ele.click()


    except:
        print('Fail,' + id)


if not Path(session_file).exists():
    driver = create_driver()
else:
    with open(session_file, 'rb') as f:
        params = pickle.load(f)
        try:
            driver = webdriver.Remote(command_executor=params["server_url"])
            driver.quit()  # 退出start_session新开的空白浏览器
            driver.session_id = params["session_id"]
            driver.execute_script('window.open("");')
            driver.switch_to.window(driver.window_handles[-1])

            with open("../stock/data/all_stock_id.txt") as file:
                for line in file:
                    dealOnePage(driver,line)
            file.close()
        except:
            driver = create_driver()
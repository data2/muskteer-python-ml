# -*- coding: utf-8 -*-
import json
import random
import time
import urllib
import requests

import scrapy


proxy_pool = []

USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 "
        "OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 "
        "Safari/534.16",
        "Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/71.0.3578.98 "
        "TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.1 "
        "LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR "
        "3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) ",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR "
        "3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/535.11 SE 2.X "
        "MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE "
        "2.X MetaSr 1.0)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 "
        "Chrome/71.0.3578.98 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 "
        "UBrowser/4.0.3214.0 Safari/537.36",
    ]

req_headers = {}

param = {
        "mergerMark": "sysapi1068"}

def parse():
        time.sleep(1)
        with open("../../stock/data/all_stock_id.txt") as file:
            code_list = file.readlines()
        file.close()
        for code in code_list:
            try:
                    param['mergerMark'] = 'sysapi1068'
                    param["paramStr"] = 'scode=' + code
                    req_headers["User-Agent"] = random.choice(USER_AGENT_LIST)
                    req_headers[
                        "Cookie"] = "JSESSIONID=66D86DD185C5A6FA420AA463FB34FB1A; insert_cookie=37836164; UC-JSESSIONID=F660392D479D21970E27E126E1B6E521; cninfo_search_record_cookie=%E5%B9%B3%E5%AE%89%E9%93%B6%E8%A1%8C; cninfo_user_browse=000001,gssz0000001,%E5%B9%B3%E5%AE%89%E9%93%B6%E8%A1%8C|000002,gssz0000002,%E4%B8%87%20%20%E7%A7%91%EF%BC%A1; _sp_id.2141=057dc973-3d84-46bc-9c65-1cdf736fd305.1577688884.7.1579090753.1579077346.c30c3d13-a460-4632-b672-8b8fd2e89c60"
                    req_headers["Origin"] = 'http://www.cninfo.com.cn'
                    req_headers["Referer"] = 'http://www.cninfo.com.cn'
                    request_url = 'http://www.cninfo.com.cn/data/project/commonInterface?' + urllib.parse.urlencode(param)
                    print(request_url)
                    res = requests.post(request_url, headers=req_headers)
                    parse_content(res.json())
                    time.sleep(10)

            except Exception as e:
                print(code + 'fail')


def parse_content(response):

        try:
            baseinfo_json = response[0]
            res = {'createDate': baseinfo_json['F001D'], 'industry': baseinfo_json['F009V'],
                   'phone': baseinfo_json['F007V'], 'fax': baseinfo_json['F008V'], 'email': baseinfo_json['F006V'],
                   'officeAddr': baseinfo_json['F005V'], 'gopublicDate': baseinfo_json['F002D'],
                   'secName': baseinfo_json['SECNAME'], 'secCode': baseinfo_json['SECCODE'],
                   'businessScope': baseinfo_json['F013V'], 'subIndustry': baseinfo_json['F010V'],
                   'registAddr': baseinfo_json['F004V'], 'mainBusiness': baseinfo_json['F012V'],
                   'website': baseinfo_json['F003V'], 'orgName': baseinfo_json['ORGNAME'],
                   'gopublicPlace': baseinfo_json['F011V'], 'name': ''.join(baseinfo_json['SECNAME'].split())}
            print(res)
            with open('../data/baseinfo.txt', "a") as file:
                file.write(str(res) + "\n")
            file.close()
        except Exception as e:
            print(e)

parse()
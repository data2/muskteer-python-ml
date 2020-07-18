import random
import urllib
import requests
import urllib3
from bs4 import BeautifulSoup

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
req_headers = {"User-Agent": random.choice(USER_AGENT_LIST),
               "Cookie": "SN_SESSION_ID=6137c805-32af-4d07-aec5-43fd0eb31028; logintp=0; _snstyxuid=8BC56592F5E78SUQ; idx_player_ap=1; PUID=272a246d8b774d98c6fe-4a0d63a688e8; ppi=302c32; Hm_lvt_7adaa440f53512a144c13de93f4c22db=1584189355; __ssar=direct%7Cdirect%7C%7C%7C; _snvd=1579088619938zVmofo0ObLf; sctx=o%3Dwww.google.com%26rp%3D%7Bd%7D0.1.5.3.0.15.1.1.0; Hm_lpvt_7adaa440f53512a144c13de93f4c22db=1584192515; __ssav=158418935533217341%7C1584189355332%7C1584192508950%7C1584192515203%7C28%7C1%7C1; __ssas=15841893553397033%7C1584192515219%7C1584192515205%7C28"}

request_urls = []
i = 1
while i <= 70:
    print(i)
    request_urls.append(
        'http://sou.pptv.com/category/typeid_1_sortType_time_pay_0_vt_3,21_pn_' + str(i))
    i = i + 1


for url in request_urls:
    print(url)
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers=req_headers)

    # print(r.data.decode())

    soup = BeautifulSoup(r.data.decode(), "lxml")

    filmList = soup.find_all(class_='content')

    for film in filmList:
        try:

            with open('pptv_free.txt', "a") as file:
                playUrl = film.find(class_='contentBox').find('a').attrs['href']
                name = film.find(class_='contentBox').find('a').find('img')['alt']
                imageUrl = film.find(class_='contentBox').find('a').find('img')['src']
                description = film.find(class_='brief').find('span').string
                secondInfo = film.find(class_='actress').find('span').string


                param = {'name': name, 'playUrl': 'http:' + playUrl, 'score': '',
                         'imageUrl': imageUrl, 'description': description,
                         'secondInfo': secondInfo,
                         'free': True, 'from': 'pptv', 'extend': {}}
                print(str(param))
                file.write(str(param) + "\n")
            file.close()
        except Exception as e:
            print(e)
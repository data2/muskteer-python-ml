import random
import urllib
import requests
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
               "Cookie": "u=1; __utma=64623162.798167061.1555766737.1555766737.1555766737.1; __utmc=64623162; __utmz=64623162.1555766737.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); JSESSIONID=A77E1A81675F92B04D8033CCBF933F15"}

request_urls = []
i = 0
while i <= 168:
    print(i)
    request_urls.append('https://v.qq.com/x/bu/pagesheet/list?_all=1&append=0&channel=movie&charge=1&listpage=2&offset='
                        + str(i*30) + '&pagesize=30&sort=18')
    i = i + 1

for url in request_urls:
    print(url)
    res = requests.get(url, req_headers)
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text, "html.parser")

    filmList = soup.find_all(class_='list_item')
    for film in filmList:
        try:
            with open('qq_free.txt', "a") as file:
                playUrl = film.find(class_='figure').attrs['href']
                name = film.find(class_='figure').attrs['title']
                imageUrl = film.find(class_='figure').find('img')['src']
                duration = film.find(class_='figure_caption').string
                score = film.find(class_='figure_score').string.strip()
                secondInfo = film.find(class_='figure_desc').string.strip()
                print(playUrl)
                param = {'name': name, 'playUrl': playUrl, 'duration': duration, 'score': score,
                         'imageUrl': 'http://' + imageUrl[2:], 'focus': '',
                         'free': True, 'from': 'qq', 'extend': {}}
                print(str(param))
                file.write(str(param) + "\n")
            file.close()
        except Exception as e:
            print('异常')




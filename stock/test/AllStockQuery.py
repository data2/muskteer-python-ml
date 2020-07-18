
import tushare as ts
import bs4
import pandas as pd


# pro = ts.pro_api()
# ts.get_stock_basics()

pro = ts.pro_api('a18f7cd446cb17f298462fa3727a580a3b1300bbcd89f00305efa046')
dataFrame = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,fullname,enname,market,exchange,curr_type,list_status,list_date,delist_date,is_hs')
print(type(dataFrame))

with open('../data/all_stock.txt', "a") as file:
    for index, stockRow in dataFrame.iterrows():
        print(index)
        dic = {'ts_code': stockRow['ts_code'],
               'symbol': stockRow['symbol'],
               'name': stockRow['name'],
               'area': stockRow['area'],
               'industry': stockRow['industry'],
               'fullname': stockRow['fullname'],
               'enname': stockRow['enname'],
               'market': stockRow['market'],
               'exchange': stockRow['exchange'],
               'curr_type': stockRow['curr_type'],
               'list_status': stockRow['list_status'],
               'list_date': stockRow['list_date'],
               'delist_date': stockRow['delist_date'],
               'is_hs': stockRow['is_hs']}
        print(dic)
        file.write(str(dic) + "\n")
    file.close()
print(len(dataFrame))



# 接口：stock_basic
# 描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
#
# 输入参数
#
# 名称	类型	必选	描述
# is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通
# list_status	str	N	上市状态： L上市 D退市 P暂停上市
# exchange	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所(未上线)
#
# 输出参数
#
# 名称	类型	描述
# ts_code	str	TS代码
# symbol	str	股票代码
# name	str	股票名称
# area	str	所在地域
# industry	str	所属行业
# fullname	str	股票全称
# enname	str	英文全称
# market	str	市场类型 （主板/中小板/创业板/科创板）
# exchange	str	交易所代码
# curr_type	str	交易货币
# list_status	str	上市状态： L上市 D退市 P暂停上市
# list_date	str	上市日期
# delist_date	str	退市日期
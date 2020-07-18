
import tushare as ts
import bs4
import pandas as pd


# pro = ts.pro_api()
# ts.get_stock_basics()

pro = ts.pro_api('a18f7cd446cb17f298462fa3727a580a3b1300bbcd89f00305efa046')
dataFrame = pro.stock_company(exchange='SSE',
                              fields='ts_code,exchange, chairman,manager,secretary,reg_capital,setup_date,province,city,introduction,website,email,office,employees,main_business,business_scope')
print(type(dataFrame))

with open('../data/all_stock_companyinfo.txt', "a") as file:
    for index, stockRow in dataFrame.iterrows():
        print(index)
        print(type(stockRow))
        dic = {'ts_code': stockRow['ts_code'],
               'exchange': stockRow['exchange'],
               'chairman': stockRow['chairman'],
               'manager': stockRow['manager'],
               'secretary': stockRow['secretary'],
               'reg_capital': stockRow['reg_capital'],
               'setup_date': stockRow['setup_date'],
               'province': stockRow['province'],
               'city': stockRow['city'],
               'introduction': stockRow['introduction'],
               'website': stockRow['website'],
               'email': stockRow['email'],
               'office': stockRow['office'],
               'employees': stockRow['employees'],
               'main_business': stockRow['main_business'],
               'business_scope': stockRow['business_scope']}
        print(dic)
        file.write(str(dic) + "\n")
    file.close()
print(len(dataFrame))

#
# 接口：stock_company
# 描述：获取上市公司基础信息
# 积分：用户需要至少120积分才可以调取，具体请参阅积分获取办法
#
# 输入参数
# 名称	类型	默认显示	描述
# exchange	str	N	交易所代码 ，SSE上交所 SZSE深交所 ，默认SSE
#
# 输出参数
# 名称	类型	默认显示	描述
# ts_code	str	Y	股票代码
# exchange	str	Y	交易所代码 ，SSE上交所 SZSE深交所
# chairman	str	Y	法人代表
# manager	str	Y	总经理
# secretary	str	Y	董秘
# reg_capital	float	Y	注册资本
# setup_date	str	Y	注册日期
# province	str	Y	所在省份
# city	str	Y	所在城市
# introduction	str	N	公司介绍
# website	str	Y	公司主页
# email	str	Y	电子邮件
# office	str	N	办公室
# employees	int	Y	员工人数
# main_business	str	N	主要业务及产品
# business_scope	str	N	经营范围
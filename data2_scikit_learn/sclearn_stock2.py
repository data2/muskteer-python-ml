import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts

begin_time = '2019-01-01'
end_time = '2019-04-30'
code = "601360"
stock = ts.get_hist_data(code, start=begin_time, end=end_time)
stock = stock.sort_index(0)  # 将数据按照日期排序下。
stock.to_pickle("stock_601360.pickle")
print("finish save ...")

# 读取股票数据分析。不用每次网络请求数据
stock = pd.read_pickle("stock_data_601360.pickle")
# 5周期、10周期、20周期和60周期
# 周线、半月线、月线和季度线
stock["5d"] = stock["close"].rolling(window=5).mean()  # 周线
stock["10d"] = stock["close"].rolling(window=10).mean()  # 半月线
stock["20d"] = stock["close"].rolling(window=20).mean()  # 月线
stock["60d"] = stock["close"].rolling(window=60).mean()  # 季度线

# print(stock.head(1))
# 展示股票收盘价格信息

stock[["close", "5d", "10d", "20d", "60d", ]].plot(figsize=(10, 6), grid=True)
plt.show()


# stock["5-10d"] = stock["5d"] - stock["10d"] #周-半月线差
# stock["5-20d"] = stock["5d"] - stock["10d"] #周-月线差
# stock[["close","5-10d","5-20d"]].plot(subplots=True, style='b', figsize=(20,10), grid=True)
# plt.show()




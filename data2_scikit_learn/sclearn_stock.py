import tushare as ts
import matplotlib.pyplot as plt
import datetime

ticker = '601360'
finace = ts.get_hist_data(ticker, '2018-01-01', '2019-04-30')
print(finace)

opens = [q for q in finace["open"]]
dates = [datetime.datetime.strptime(q, "%Y-%m-%d") for q in finace.index]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot_date(dates, opens, '-')
fig.autofmt_xdate()
plt.show()
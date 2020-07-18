import json

import matplotlib.pyplot as plt

x = []
y = []

d = {}
with open("test.txt", "rt", encoding="UTF-8") as f:
    d = json.load(f)
f.close()

# 具体指标
wdnodes = d['returndata']['wdnodes'][0]['nodes']
# 具体数据
datanodes = d['returndata']['datanodes']
for datastr in datanodes:
    if datastr['code'].find('A0G0804') > 0:
        if datastr['data']['data'] != 0:
            x.append(datastr['code'][-4:])
            y.append(datastr['data']['data'])
print(x)
print(y)

# 正常显示中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 绘图，设置(label)图例名字为'第一条线'，显示图例plt.legend()
x.reverse()
plt.plot(x, y, label='第一条线')

# x轴标签
plt.xlabel('年份')
# y轴标签
plt.ylabel('数量')

# 可视化图标题
plt.title('指标数量')

# 显示图例
plt.legend()
# 显示图形
plt.show()

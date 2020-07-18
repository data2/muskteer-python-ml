#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv

from twisted.python.compat import raw_input

# console io
# str = raw_input("请输入：")
# print("你输入的内容是: %s" % str)


# file io
# with open("test.txt", "a") as file:
#     file.write("hi\n")
#     file.write("py\n")
# file.close()

# with open("test.txt", "r") as file:
#     # print(file.readlines())
#     # file.seek(0)
#     str2 = file.readline()
#     while str2:
#         print(str2)
#         str2 = file.readline()
# file.close()


# csv io
# header = ["序号", "数值"]
# data = ["1", "1000"]
# data2 = [["2", "1000"],["3","999"]]
# with open("test.csv", "w", newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(data)
#     writer.writerows(data2)
#     f.close()

data = []
with open("test.csv", encoding="gbk") as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        data.append(row)
print(header)
print(data)
csvfile.close()

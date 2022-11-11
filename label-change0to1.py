# 导入工具包
import pandas as pd
import numpy as np
import os

# 标签第一个类别序号改变
# 路径
path = 'F://test/open-fire-10000/open_label/'

# 文件列表
files = []
dataMat = []
newData1 = []
newData2 = []

for file in os.listdir(path):
    if file.endswith(".txt"):
        files.append(path + file)
print(files)


# 遍历所有文件
for file in files:
    file_in = open(file)
    print("file_in.name:", file_in.name)

    for line in file_in.readlines():
        curLine = line.strip().split(" ")
        dataMat.append(curLine)
    print('dataMat:', dataMat)
    x = len(dataMat)        # 多少行
    y = len(dataMat[0])     # dataMat是一行多个数据 0 1 2 3 4 。。。。。
    print(x)
    print(y)

    for i in range(x):
        for j in range(y):
            data0 = float(dataMat[i][0])
            data1 = float(dataMat[i][1])
            data2 = float(dataMat[i][2])
            data3 = float(dataMat[i][3])
            data4 = float(dataMat[i][4])

            if data0 == 15:
                newData1 = ['0', data1, data2, data3, data4]
            elif data0 == 16:
                newData1 = ['1', data1, data2, data3, data4]
            else:
                newData1 = [data0, data1, data2, data3, data4]
        newData2.append(newData1)
    print(newData2)
    file_in.close()


    file_out = open(file, 'w')

    for i in range(x):
        for j in range(y):
            if j > 0 and j % 4 == 0:
                file_out.write(str((newData2[i][j])) + '\n')
            else:
                file_out.write(str((newData2[i][j])) + ' ')

    file_out.close()

    dataMat.clear()
    newData2.clear()
    newData1.clear()


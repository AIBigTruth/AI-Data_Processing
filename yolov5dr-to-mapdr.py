# 导入工具包
import pandas as pd
import numpy as np
import os
# import data

# yolov5的detect.py测试出来的label里面的文件转化为真实框的格式（类别，置信度，左上角x，左上角y，右下角x，右下角y）
# 修改3069和2048，这是图片得固定长宽。所以应该保证图片大小一样，不然要读取图片大小，然后设置参数
# 注意文件备份，程序跑通直接修改原文件
# 路径
# path = 'F://bitbucket/yolov5/runs/detect/exp33/labels/'

path ='F://github/yolov5-v5/runs/detect/detect-fire-smoke-4/labels/'


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
    x = len(dataMat)
    y = len(dataMat[0])
    print(x)
    print(y)
    w = 1
    h = 1
    # x2  x1 是3069，y2 y1 是2048
    for i in range(x):
        for j in range(y):
            x2 = (2 * w * float(dataMat[i][1]) + w * float(dataMat[i][3])) / 2
            x1 = (2 * w * float(dataMat[i][1]) - w * float(dataMat[i][3])) / 2
            y2 = (2 * h * float(dataMat[i][2]) + h * float(dataMat[i][4])) / 2
            y1 = (2 * h * float(dataMat[i][2]) - h * float(dataMat[i][4])) / 2
            r = float(dataMat[i][5])
            c = float(dataMat[i][0])
            if c == 0:
                newData1 = ['fire', r, int(x1), int(y1), int(x2), int(y2)]
            else:
                newData1 = ['smoke', r, int(x1), int(y1), int(x2), int(y2)]

        newData2.append(newData1)
    print(newData2)
    file_in.close()


    file_out = open(file, 'w')

    for i in range(x):
        for j in range(y):
            if j > 0 and j % 5 == 0:
                file_out.write(str((newData2[i][j])) + '\n')
            else:
                file_out.write(str((newData2[i][j])) + ' ')

    file_out.close()

    dataMat.clear()
    newData2.clear()
    newData1.clear()


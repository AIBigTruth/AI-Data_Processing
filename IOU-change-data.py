# 导入工具包
import pandas as pd
import numpy as np
import os
# import data

# yolov5 fire-smoke-dll工程跑出的检测结果格式为（x,y,w，h）,为了计算IOU，需要将其转化为（左上角x，左上角y，右下角x，右下角y）
# IOU计算需要，
# 注意文件备份，程序跑通直接修改原文件
# 路径
# path = 'F://bitbucket/yolov5/runs/detect/exp33/labels/'

path ='F://github/yolov5-jushi/Distance/fire15-avi-IOU/'
# path ='F://github/yolov5-jushi/Distance/lighter-IOU/'


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
    # （x,y,w，h）
    for i in range(x):
        for j in range(y):
            x0 = (2 * w * float(dataMat[i][0]) - w * float(dataMat[i][2])) / 2
            y0 = (2 * h * float(dataMat[i][1]) - h * float(dataMat[i][3])) / 2
            x1 = (2 * w * float(dataMat[i][0]) + w * float(dataMat[i][2])) / 2
            y1 = (2 * h * float(dataMat[i][1]) + h * float(dataMat[i][3])) / 2

            newData1 = [x0, y0, x1, y1]


        newData2.append(newData1)
    print(newData2)
    file_in.close()


    file_out = open(file, 'w')

    for i in range(x):
        for j in range(y):
            if j > 0 and j % 3 == 0:
                file_out.write(str((newData2[i][j])) + '\n')
            else:
                file_out.write(str((newData2[i][j])) + ' ')

    file_out.close()

    dataMat.clear()
    newData2.clear()
    newData1.clear()


# 导入工具包
import pandas as pd
import numpy as np
import os
# import data

#打标签的时候以空格名字命名，如other clothes，mAP的时候格式不符合，不能空格，古修改这类名称为other_clothes

# 路径
# path = 'F://bitbucket/yolov5/runs/detect/exp33/labels/'

path ='F://github/yolov5-v5/runs/detect/detect-clothes-hat-2/ground-truth/'


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

    # x=6,即一个txt里面6行，即6个目标
    for i in range(x):
        if len(dataMat[i]) == 6:
            name = dataMat[i][0] + "_" + dataMat[i][1]
            print('name:', name)
            newData1 = [name, dataMat[i][2], dataMat[i][3], dataMat[i][4], dataMat[i][5]]
        else:
            newData1 = [dataMat[i][0], dataMat[i][1], dataMat[i][2], dataMat[i][3], dataMat[i][4]]
        newData2.append(newData1)
    print("newData2: ", newData2)
    file_in.close()


    file_out = open(file, 'w')

    for i in range(x):
        for j in range(5):
            if j > 0 and j % 4 == 0:
                file_out.write(str((newData2[i][j])) + '\n')
            else:
                file_out.write(str((newData2[i][j])) + ' ')

    file_out.close()

    dataMat.clear()
    newData2.clear()
    newData1.clear()


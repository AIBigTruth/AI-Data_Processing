# 导入工具包
import pandas as pd
import numpy as np
import os
import cv2
# import data


# yolov5的detect.py测试出来的label里面的文件转化为真实框的格式（类别，置信度，左上角x，左上角y，右下角x，右下角y）
# 修改3069和2048，这是图片得固定长宽。所以应该保证图片大小一样，不然要读取图片大小，然后设置参数
# 注意文件备份，程序跑通直接修改原文件
# 路径
# path = 'F://bitbucket/yolov5/runs/detect/exp33/labels/'

path ='F://github/yolov5-v5/runs/detect/detect-clothes-hat-221-0.5-test/labels/'
path_image ='F://github/yolov5-v5/runs/detect/detect-clothes-hat-221-0.5-test/image/'

# 文件列表
files = []
images = []
ws = []
hs = []
dataMat = []
newData1 = []
newData2 = []
num = -1

# 获取文件路径而已
for file in os.listdir(path):
    if file.endswith(".txt"):
        files.append(path + file)
print("files: ", files)

for image in os.listdir(path_image):
    if image.endswith(".jpg"):
        images.append(path_image + image)
print("images: ", images)

for image in images:
    image_in = cv2.imread(image)
    size = image_in.shape
    w = size[1]
    h = size[0]
    ws.append(w)
    hs.append(h)
print("ws: ", ws)
print("hs: ", hs)
len_ws = len(ws)
len_hs = len(hs)
print("len_ws: ", len_ws)
print("len_hs: ", len_hs)

# 遍历所有文件
for file in files:
    num = num + 1
    print("num: ", num)
    print("ws[num]: ", ws[num])
    print("hs[num] ", hs[num])


    file_in = open(file)
    print("file_in.name: ", file_in.name)

    for line in file_in.readlines():
        curLine = line.strip().split(" ")
        dataMat.append(curLine)
    print('dataMat: ', dataMat)
    x = len(dataMat)
    y = len(dataMat[0])
    print("x: ", x)
    print("y: ", y)

    for i in range(x):
        for j in range(y):
            x2 = (2 * ws[num] * float(dataMat[i][1]) + ws[num] * float(dataMat[i][3])) / 2
            x1 = (2 * ws[num] * float(dataMat[i][1]) - ws[num] * float(dataMat[i][3])) / 2
            y2 = (2 * hs[num] * float(dataMat[i][2]) + hs[num] * float(dataMat[i][4])) / 2
            y1 = (2 * hs[num] * float(dataMat[i][2]) - hs[num] * float(dataMat[i][4])) / 2
            r = float(dataMat[i][5])
            c = float(dataMat[i][0])
            if c == 0:
                newData1 = ['red', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 1:
                newData1 = ['orange', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 2:
                newData1 = ['yellow', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 3:
                newData1 = ['green', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 4:
                newData1 = ['blue', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 5:
                newData1 = ['none', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 6:
                newData1 = ['white', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 7:
                newData1 = ['work_clothes', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 8:
                newData1 = ['work_pants', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 9:
                newData1 = ['other_pants', r, int(x1), int(y1), int(x2), int(y2)]
            elif c == 10:
                newData1 = ['other_clothes', r, int(x1), int(y1), int(x2), int(y2)]
            else:
                newData1 = ['open_clothes', r, int(x1), int(y1), int(x2), int(y2)]

        newData2.append(newData1)
    print("newData2: ", newData2)
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


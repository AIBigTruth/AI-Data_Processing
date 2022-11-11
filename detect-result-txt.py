import os
import cv2
import numpy as np
import torch
import sys
import math

# 检测结果的lable格式转化，从（class,c,x,y,w,h）-》（类别，置信度，左上角x，左上角y，右下角x，右下角y）


file_in = open('F://bitbucket/yolov5/runs/detect/exp31/labels/879.txt')
print("name:", file_in.name)

dataMat = []
for line in file_in.readlines():
    curLine = line.strip().split(" ")
    dataMat.append(curLine)
print('dataMat:', dataMat)
x = len(dataMat)
y = len(dataMat[0])
print(x)
print(y)

newData1 = []
newData2 = []

for i in range(x):
	for j in range(y):
		x2 = (2 * 3069 * float(dataMat[i][1]) + 3069 * float(dataMat[i][3]))/2
		x1 = (2 * 3069 * float(dataMat[i][1]) - 3069 * float(dataMat[i][3]))/2
		y2 = (2 * 2048 * float(dataMat[i][2]) + 2048 * float(dataMat[i][4]))/2
		y1 = (2 * 2048 * float(dataMat[i][2]) - 2048 * float(dataMat[i][4]))/2
		c = float(dataMat[i][5])
		newData1 = ['bad', c, int(x1), int(y1), int(x2), int(y2)]
	newData2.append(newData1)
print(newData2)

file_out = open('data.txt', 'w')

for i in range(x):
	for j in range(y):
		if j > 0 and j % 5 == 0:
			file_out.write(str((newData2[i][j])) + '\n')
		else:
			file_out.write(str((newData2[i][j])) + ' ')

file_out.close()









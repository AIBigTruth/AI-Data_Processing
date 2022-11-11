# 导入工具包
import numpy as np
import os

# # 得出yolov5检测结果的两个框四个坐标的欧式距离，一张图片里面只有一个目标

# 路径
# path = 'F://bitbucket/yolov5/runs/detect/exp33/labels/'

# path ='F://github/yolov5-jushi/Distance/fire21-avi/'
path ='F://github/yolov5-jushi/Distance/fire11-mp4-IOU/'
# cpath ='F://github/yolov5-jushi/Distance/lighter/'


# 文件列表
files = []
dataMat = []
oneDatas = []
twoDatas = []
oneData = []
twoData = []
distanceDatas = []
fiveData =[]
fiveDatas =[]

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
    y = len(dataMat[0])   # 4
    print('len(dataMat):', len(dataMat))
    print('len(dataMat[0])', len(dataMat[0]))

    num = 1  # 若是fire-smoke程序已经进行抽帧，这里就是1。弱之前没有抽帧，也可改变这个参数进行抽帧。
    threshold = 20
    # 取出frame为5的倍数的帧
    for i in range(x):
        if (i % num) == 0:
            fiveData = [int(dataMat[i][0]), int(dataMat[i][1]), int(dataMat[i][2]), int(dataMat[i][3])]
            fiveDatas.append(fiveData)
    print('fiveDatas:', fiveDatas)
    print('len(fiveDatas):', len(fiveDatas))

    file_in.close()

    for i in range(len(fiveDatas)):
        if i < (len(fiveDatas)-1):
            distance = round(np.sqrt(
                np.power((fiveDatas[i][0] - fiveDatas[i+1][0]), 2) + np.power((fiveDatas[i][1] - fiveDatas[i+1][1]), 2) +
                np.power((fiveDatas[i][2] - fiveDatas[i+1][2]), 2) + np.power((fiveDatas[i][3] - fiveDatas[i+1][3]), 2)), 1)
            if distance < threshold:
                distanceDatas.append(distance)
    print('distanceDatas:', distanceDatas)
    print('len(distanceDatas):', len(distanceDatas))
    meanDistance = np.mean(distanceDatas)
    print('meanDistance:', meanDistance)
    print('maxDistance:', max(distanceDatas))
    print('minDistance:', min(distanceDatas))




    # dataMat.clear()
    # oneDatas.clear()
    # newData1.clear()



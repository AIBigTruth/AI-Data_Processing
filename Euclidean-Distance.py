# 导入工具包
import numpy as np
import os

# # 得出yolov5检测结果的两个框四个坐标的欧式距离，一张图片里面只有一个目标

# 路径
# path = 'F://bitbucket/yolov5/runs/detect/exp33/labels/'

path ='F://github/yolov5-jushi/Distance/fire13-avi/'
# path ='F://github/yolov5-jushi/Distance/fire12-mp4/'
# path ='F://github/yolov5-jushi/Distance/lighter/'


# 文件列表
files = []
dataMat = []
oneDatas = []
twoDatas = []
oneData = []
twoData = []
distanceDatas = []

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

    #
    for i in range(x):
        if (i % 2) != 0:   # one
            twoData = [int(dataMat[i][0]), int(dataMat[i][1]), int(dataMat[i][2]), int(dataMat[i][3])]
            twoDatas.append(twoData)

        else:
            oneData = [int(dataMat[i][0]), int(dataMat[i][1]), int(dataMat[i][2]), int(dataMat[i][3])]
            oneDatas.append(oneData)

    print('oneDatas:', oneDatas)
    print('twoDatas:', twoDatas)

    print('len(oneDatas):', len(oneDatas))
    print('len(twoDatas)', len(twoDatas))

    file_in.close()


    if len(oneDatas) == len(oneDatas):
        for i in range(len(oneDatas)):
            distance = round(np.sqrt(
                np.power((oneDatas[i][0] - twoDatas[i][0]), 2) + np.power((oneDatas[i][1] - twoDatas[i][1]), 2) +
                np.power((oneDatas[i][2] - twoDatas[i][2]), 2) + np.power((oneDatas[i][3] - twoDatas[i][3]), 2)), 1)

            if distance < 20:
                distanceDatas.append(distance)
        print('distanceDatas:', distanceDatas)
        print('len(distanceDatas):', len(distanceDatas))
        meanDistance = np.mean(distanceDatas)
        print('meanDistance:', meanDistance)
        print('maxDistance:', max(distanceDatas))
        print('minDistance:', min(distanceDatas))

    else:
        if len(oneDatas) > len(twoDatas):
            del oneDatas[len(oneDatas) - 1]
            for i in range(len(twoDatas)):
                distance = round(np.sqrt(
                    np.power((oneDatas[i][0] - twoDatas[i][0]), 2) + np.power((oneDatas[i][1] - twoDatas[i][1]), 2) +
                    np.power((oneDatas[i][2] - twoDatas[i][2]), 2) + np.power((oneDatas[i][3] - twoDatas[i][3]), 2)), 1)
                if distance < 20:
                    distanceDatas.append(distance)
            print('distanceDatas:', distanceDatas)
            print('len(distanceDatas):', len(distanceDatas))
            meanDistance = np.mean(distanceDatas)
            print('meanDistance:', meanDistance)
            print('maxDistance:', max(distanceDatas))
            print('minDistance:', min(distanceDatas))

        else:
            del twoDatas[len(twoDatas) - 1]
            for i in range(len(oneDatas)):
                distance = round(np.sqrt(
                    np.power((oneDatas[i][0] - twoDatas[i][0]), 2) + np.power((oneDatas[i][1] - twoDatas[i][1]), 2) +
                    np.power((oneDatas[i][2] - twoDatas[i][2]), 2) + np.power((oneDatas[i][3] - twoDatas[i][3]), 2)), 1)
                if distance < 20:
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



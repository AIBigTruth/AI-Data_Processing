# 导入工具包
import numpy as np
import os

# # 得出yolov5检测结果的两个框四个坐标的欧式距离，一张图片里面只有一个目标

# 路径
# path = 'F://bitbucket/yolov5/runs/detect/exp33/labels/'

# path ='F://github/yolov5-jushi/Distance/fire21-avi/'
path ='F://github/yolov5-jushi/Distance/fire21-avi-IOU-10/'
# path ='F://github/yolov5-jushi/Distance/lighter-IOU/'

def compute_iou(rec1, rec2):
    """
    computing IoU
    :param rec1: (y0, x0, y1, x1), which reflects   ×不用这个坐标格式
            (top, left, bottom, right)
    :param rec2: (y0, x0, y1, x1)
    :return: scala value of IoU


    (x0, y0, x1, y1)    √用这个坐标格式    0-1,2-3互换一下
    rec_1:左上角(rec_1[0],rec_1[1])    右下角：(rec_1[2],rec_1[3])
    rec_2:左上角(rec_2[0],rec_2[1])    右下角：(rec_2[2],rec_2[3])

    （rec_1）
    1--------1
    1   1----1------1
    1---1----1      1
        1           1
        1-----------1 （rec_2）
    IOU = AnB/AuB
    """
    # computing area of each rectangles
    #  (x0, y0, x1, y1)
    S_rec1 = (rec1[3] - rec1[1]) * (rec1[2] - rec1[0])   # 第一个bbox面积 = 长×宽
    S_rec2 = (rec2[3] - rec2[1]) * (rec2[2] - rec2[0])   # 第二个bbox面积 = 长×宽

    # computing the sum_area
    sum_area = S_rec1 + S_rec2  # 总面积 交集计算了两次，之后要减掉交集一次

    # find the each edge of intersect rectangle  交集
    left_line = max(rec1[0], rec2[0])     # 交集左上角顶点横坐标
    right_line = min(rec1[2], rec2[2])    # 交集右下角顶点横坐标
    top_line = max(rec1[1], rec2[1])      # 交集左上角顶点纵坐标
    bottom_line = min(rec1[3], rec2[3])   # 交集右下角顶点纵坐标

    # judge if there is an intersect   # 不存在并集的情况
    if left_line >= right_line or top_line >= bottom_line:   # 左边的线>右边的线，或者上面的线>下面的线。。。图是左上角为0，右为正x,下为正y
        return 0
    else:
        intersect = (right_line - left_line) * (bottom_line - top_line)   #  长*宽，是交集的面积
        return (intersect / (sum_area - intersect)) * 1.0


# 文件列表
files = []
dataMat = []
oneDatas = []
twoDatas = []
oneData = []
twoData = []
distanceDatas = []
iouDatas = []
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

    num = 10   # 若是fire-smoke程序已经进行抽帧，这里就是1。若之前没有抽帧，也可改变这个参数进行抽帧。
    threshold = 2000
    # 取出frame为5的倍数的帧
    for i in range(x):
        if (i % num) == 0:
            fiveData = [float(dataMat[i][0]), float(dataMat[i][1]), float(dataMat[i][2]), float(dataMat[i][3])]
            fiveDatas.append(fiveData)
    print('fiveDatas:', fiveDatas)
    print('len(fiveDatas):', len(fiveDatas))

    file_in.close()

    for i in range(len(fiveDatas)):
        if i < (len(fiveDatas)-1):
            iou = compute_iou(fiveDatas[i], fiveDatas[i+1])

            if iou < threshold:
                iouDatas.append(iou)
    print('iouDatas:', iouDatas)
    print('len(iouDatas):', len(iouDatas))
    meanIOU = np.mean(iouDatas)
    print('meanDistance:', meanIOU)
    print('maxDistance:', max(iouDatas))
    print('minDistance:', min(iouDatas))




    # dataMat.clear()
    # oneDatas.clear()
    # newData1.clear()



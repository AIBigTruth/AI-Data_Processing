# coding=gbk
import os
import random

# 训练之前，将图片随机打乱，之后进行打标,标签要严格对应图片名称


#path_image：图片路径
#path_label: 标签路径
#filename：修改前的文件名
#n：随机数序号（和修改后的文件名有关）
def rename(path_image, path_label, resultList):
    count_image = 0
    count_label = 0
    imagelist=os.listdir(path_image)
    labellist = os.listdir(path_label)

    #确保图片和标签用到同一个名称
    #图片随机命名与排序
    print("image random: ")
    for folder_image in imagelist:
        folder_image = str(folder_image)
        nowPath_image = path_image + "/" + folder_image

        targetfolder_image = str(resultList[count_image])
        targetPath_image = path_image + "/" + targetfolder_image
        os.rename(nowPath_image, targetPath_image + ".jpg")
        print(folder_image + "->" + targetfolder_image + ".jpg")
        count_image += 1

    print("label random: ")
    #标签随机命名与排序
    for folder_label in labellist:
        folder_label = str(folder_label)
        nowPath_label = path_label + "/" + folder_label

        targetfolder_label = str(resultList[count_label])
        targetPath_label = path_label + "/" + targetfolder_label
        os.rename(nowPath_label, targetPath_label + ".txt")
        print(folder_label + "->" + targetfolder_label + ".txt")
        count_label += 1
    return count_image, count_label

resultList = []  # 用于存放结果的List
A = 10000  # 最小随机数   6000
B = 14500  # 最大随机数   6014
COUNT = 4500

# 利用Python中的randomw.sample()函数实现
resultList = random.sample(range(A, B + 1), COUNT)     # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。
print(resultList)  # 打印结果

#文件夹分布在多个文件，逐个输入。输出的文件夹首尾相接。
path_image = "F://test/random-data/image"
path_label = "F://test/random-data/label"
print(path_image)
a, b = rename(path_image, path_label, resultList)


# path="D:\\val"
# print(path)
# b=rename(path,resultList,a)

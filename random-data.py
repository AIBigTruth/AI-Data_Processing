# coding=gbk
import os
import random

# 训练之前，将图片随机打乱，之后进行打标
# 保存的文件加格式的话.jpg，需要保证随机前和随机后没有重复命名


#path：文件路径
#filename：修改前的文件名
#n：随机数序号（和修改后的文件名有关）
def rename(path,resultList):
    count = 0
    folderlist=os.listdir(path)
    for folder in folderlist:
        folder = str(folder)
        nowPath = path+"/"+folder

        targetfolder=str(resultList[count])
        targetPath = path +"/"+ targetfolder
        os.rename(nowPath, targetPath + ".jpg")
        print(folder+" -> "+ targetfolder + ".jpg")
        count+=1
    return count

resultList = []  # 用于存放结果的List
A = 6000  # 最小随机数
B = 6014  # 最大随机数
COUNT = 14
#n=0
# 利用Python中的randomw.sample()函数实现
resultList = random.sample(range(A, B + 1), COUNT)     # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。
print(resultList)  # 打印结果

#文件夹分布在多个文件，逐个输入。输出的文件夹首尾相接。
path="F://test/random-data/xz"
print(path)
a=rename(path,resultList)


# path="D:\\val"
# print(path)
# b=rename(path,resultList,a)

# coding=gbk
import os
import random

# ѵ��֮ǰ����ͼƬ������ң�֮����д��,��ǩҪ�ϸ��ӦͼƬ����


#path_image��ͼƬ·��
#path_label: ��ǩ·��
#filename���޸�ǰ���ļ���
#n���������ţ����޸ĺ���ļ����йأ�
def rename(path_image, path_label, resultList):
    count_image = 0
    count_label = 0
    imagelist=os.listdir(path_image)
    labellist = os.listdir(path_label)

    #ȷ��ͼƬ�ͱ�ǩ�õ�ͬһ������
    #ͼƬ�������������
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
    #��ǩ�������������
    for folder_label in labellist:
        folder_label = str(folder_label)
        nowPath_label = path_label + "/" + folder_label

        targetfolder_label = str(resultList[count_label])
        targetPath_label = path_label + "/" + targetfolder_label
        os.rename(nowPath_label, targetPath_label + ".txt")
        print(folder_label + "->" + targetfolder_label + ".txt")
        count_label += 1
    return count_image, count_label

resultList = []  # ���ڴ�Ž����List
A = 10000  # ��С�����   6000
B = 14500  # ��������   6014
COUNT = 4500

# ����Python�е�randomw.sample()����ʵ��
resultList = random.sample(range(A, B + 1), COUNT)     # sample(x,y)�����������Ǵ�����x�У����ѡ��y�����ظ���Ԫ�ء�
print(resultList)  # ��ӡ���

#�ļ��зֲ��ڶ���ļ���������롣������ļ�����β��ӡ�
path_image = "F://test/random-data/image"
path_label = "F://test/random-data/label"
print(path_image)
a, b = rename(path_image, path_label, resultList)


# path="D:\\val"
# print(path)
# b=rename(path,resultList,a)

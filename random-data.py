# coding=gbk
import os
import random

# ѵ��֮ǰ����ͼƬ������ң�֮����д��
# ������ļ��Ӹ�ʽ�Ļ�.jpg����Ҫ��֤���ǰ�������û���ظ�����


#path���ļ�·��
#filename���޸�ǰ���ļ���
#n���������ţ����޸ĺ���ļ����йأ�
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

resultList = []  # ���ڴ�Ž����List
A = 6000  # ��С�����
B = 6014  # ��������
COUNT = 14
#n=0
# ����Python�е�randomw.sample()����ʵ��
resultList = random.sample(range(A, B + 1), COUNT)     # sample(x,y)�����������Ǵ�����x�У����ѡ��y�����ظ���Ԫ�ء�
print(resultList)  # ��ӡ���

#�ļ��зֲ��ڶ���ļ���������롣������ļ�����β��ӡ�
path="F://test/random-data/xz"
print(path)
a=rename(path,resultList)


# path="D:\\val"
# print(path)
# b=rename(path,resultList,a)

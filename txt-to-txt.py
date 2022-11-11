import shutil
import os
# 文件批量读取转移目录或删除批量文件，鸡蛋里挑骨头。
# f2.write(ff)

#path_in = 'F://bitbucket/yolo3-pytorch-b/VOCdevkit/Annotations-bccd/'
#path_out = 'F://bitbucket/yolo3-pytorch-b/VOCdevkit/Annotations-bccd-txt/'
path_in = 'F:\\test\\workclothes-hat\\Annotations\\'
path_out = 'F:\\test\\workclothes-hat\\Annotations-txt\\'

#path_in = 'F:\\test\\text5\\'
#path_out = 'F:\\test\\text5-txt\\'

texts = os.listdir(path_in)
ll = []
for text in texts:
    if text[-3:] == 'txt':
        ll.append(text)
for name in ll:
    with open(path_in+name, 'r') as f1:
        ff = f1.read()
    with open(path_out+name, 'w') as f2:
        f2.write(ff)
print('finish!')



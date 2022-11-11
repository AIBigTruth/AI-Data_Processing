import glob
import os
import xml.etree.ElementTree as ET
import shutil

# 查找xml中有black_smoke的文件，并把图片和文件都复制出来，进行调整。
# 查找xml中有white_smoke的文件，并把图片和文件都复制出来，进行数据增强

xml_path = 'F://test/find-file/dst-label/'
image_path = 'F://test/find-file/image/'
dst_xml_path = 'F://test/find-file/dst-label/'
dst_image_path = 'F://test/find-file/dst-image/'


#接下来是写入txt文件中
if __name__ == '__main__':

    count_name = 0
    count_xmlname = 0
    count_black_smoke = 0
    black_smoke_file = []
    jpg_list = []
    xml_list = []
    jpg_name_list = []
    xml_name_list = []

    #定义一个空的字符串
    t = ''
    #获取所有的xml文件路径
    allfilepath = []
    for file in os.listdir(xml_path):
        if file.endswith('.xml'):
            file = os.path.join(xml_path, file)
            allfilepath.append(file)
        else:
            pass
     #生成需要的对应xml文件名的txt
    for file in allfilepath:
        tree = ET.parse(file)
        # 统计颜色数量

        for obj in tree.findall('object'):
            # 获取name，我上边的实例图片中的红色区域
            name = obj.find('name').text
            # 修改label，这里是不同数据集大融合的关键
            if name == 'black_smoke':
                black_smoke_file.append(file)
                count_black_smoke = count_black_smoke + 1
            else:
                pass
    print('file: ', black_smoke_file)
    print('file.count(): ', len(black_smoke_file))
    print('num: ', count_black_smoke)















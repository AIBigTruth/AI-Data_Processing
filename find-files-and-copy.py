import glob
import os
import xml.etree.ElementTree as ET
import shutil

# 查找xml中有black_smoke的文件，并把图片和文件都复制出来，进行调整。
# 查找xml中有white_smoke的文件，并把图片和文件都复制出来，进行数据增强

xml_path = 'F://test/find-file/label/'
image_path = 'F://test/find-file/image/'
dst_xml_path = 'F://test/find-file/dst-label/'
dst_image_path = 'F://test/find-file/dst-image/'


#接下来是写入txt文件中
if __name__ == '__main__':

    count_name = 0
    count_xmlname = 0
    count_black_smoke = 0
    count_white_smoke = 0
    black_smoke_file = []
    white_smoke_file = []
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
            if name == 'white_smoke':
                white_smoke_file.append(file)
                count_white_smoke = count_white_smoke + 1
            else:
                pass
    # print('file: ', white_smoke_file)
    print('file.count(): ', len(white_smoke_file))
    print('num: ', count_white_smoke)

    for name in white_smoke_file:
        count_name = count_name + 1
        path = name
        shutil.copy(path, dst_xml_path)
    print('count_name: ', count_name)

    # 从black_smoke_file获取文件名称
    for name1 in white_smoke_file:
        if os.path.splitext(name1)[1] == '.xml':
            xml_list.append(os.path.splitext(name1)[0])

    print('xml_list: ',   xml_list)
    print('xml_list_len: ', len(xml_list))
    print('xml_list_one_len: ', len(xml_list[0]))
    print('j: ', (xml_list[0]))
    print('j: ', (xml_list[0])[25:42])
    for name2 in xml_list:
        xml_name_list.append(name2[25:42])

    print('jpg_name_list: ', xml_name_list)
    print('jpg_name_list_len: ', len(xml_name_list))

    # 复制图片
    for xmlname in xml_name_list:
        count_xmlname = count_xmlname + 1
        path = image_path + xmlname + '.jpg'
        # print('path: ', path)
        shutil.copy(path, dst_image_path)
    print('count_xmlname: ', count_xmlname)




    # for root, dirs, files in os.walk(image_path):
    #     for file in files:
    #         if os.path.splitext(file)[1] == '.jpg':
    #           jpg_list.append(os.path.splitext(file)[0])
    #
    # # print('jpg_list: ', jpg_list)
    # print("len(jpg_list): ", len(jpg_list))









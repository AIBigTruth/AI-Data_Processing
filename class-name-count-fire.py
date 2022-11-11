import glob
import os

# 统计类别个数，排除打错标签了

# xml_path = 'F:\\test\\Annotations-down'
# xml_path = 'F:\\test\\FallDataset_300_xml_rename'
# xml_path = 'F://test/make label/12-fire-smoke-white/label'
xml_path = 'F://test/find-file/dst-label'
# F://创悦诚/工作服安全帽/安全帽-1/Annotations


#定义从xml获取信息的函数
def _read_anno(filename, count_fire, count_white_smoke,  count_black_smoke, count_other):

    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    #统计颜色数量

    for obj in tree.findall('object'):
    	#获取name，我上边的实例图片中的红色区域
        name = obj.find('name').text
        #修改label，这里是不同数据集大融合的关键
        if name == 'fire':
            count_fire = count_fire + 1
        elif name == 'white_smoke':
            count_white_smoke = count_white_smoke + 1
        elif name == 'black_smoke':
            count_black_smoke = count_black_smoke + 1

        else:
            count_other = count_other + 1
            print(name)

    objects = [count_fire,  count_white_smoke,  count_black_smoke, count_other]

    return objects



#接下来是写入txt文件中
if __name__ == '__main__':

    count_fire = 0
    count_white_smoke = 0
    count_black_smoke = 0
    count_other = 0

    count_all = [0,  0, 0, 0]
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

        result = _read_anno(file, count_fire, count_white_smoke, count_black_smoke, count_other)
        count_all = [count_all[i]+result[i] for i in range(0, len(result))]


    print(result)
    print(count_all)


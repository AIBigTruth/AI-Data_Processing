import glob
import os

# 统计类别个数，排除打错标签了


# xml_path = 'F:\\test\\Annotations-down'
# xml_path = 'F:\\test\\FallDataset_300_xml_rename'
xml_path = 'F:\\test\\workclothes-hat\\Annotations'
# F://创悦诚/工作服安全帽/安全帽-1/Annotations


#定义从xml获取信息的函数
def _read_anno(filename, count_red, count_orange,  count_yellow, count_green, count_blue, count_none,
                            count_white, count_workclothes, count_workpants, count_otherclothes, count_otherpants,
                            count_openclothes, count_other):

    import xml.etree.ElementTree as ET
    tree = ET.parse(filename)
    #统计颜色数量

    for obj in tree.findall('object'):
    	#获取name，我上边的实例图片中的红色区域
        name = obj.find('name').text
        #修改label，这里是不同数据集大融合的关键
        if name == 'red':
            count_red = count_red + 1
        elif name == 'orange':
            count_orange = count_orange + 1
        elif name == 'yellow':
            count_yellow = count_yellow + 1
        elif name == 'green':
            count_green = count_green + 1
        elif name == 'blue':
            count_blue = count_blue + 1
        elif name == 'none':
            count_none = count_none + 1
        elif name == 'white':
            count_white = count_white + 1
        elif name == 'work clothes':
            count_workclothes = count_workclothes + 1
        elif name == 'work pants':
            count_workpants = count_workpants + 1
        elif name == 'other clothes':
            count_otherclothes = count_otherclothes + 1
        elif name == 'other pants':
            count_otherpants = count_otherpants + 1
        elif name == 'open clothes':
            count_openclothes = count_openclothes + 1
        else:
            count_other = count_other + 1
            print(name)

    objects = [count_red, count_orange,  count_yellow, count_green, count_blue, count_none,
                            count_white, count_workclothes, count_workpants, count_otherclothes, count_otherpants,
                            count_openclothes, count_other]

    return objects



#接下来是写入txt文件中
if __name__ == '__main__':

    count_red = 0
    count_orange = 0
    count_yellow = 0
    count_green = 0
    count_blue = 0
    count_none = 0
    count_white = 0

    count_workclothes = 0
    count_workpants = 0
    count_otherclothes = 0
    count_otherpants = 0
    count_openclothes = 0

    count_other = 0
    count_all = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

        result = _read_anno(file, count_red, count_orange,  count_yellow, count_green, count_blue, count_none,
                            count_white, count_workclothes, count_workpants, count_otherclothes, count_otherpants,
                            count_openclothes, count_other)
        count_all = [count_all[i]+result[i] for i in range(0,len(result))]


    print(result)
    print(count_all)


import os

# 两个文件名称比较,先删除image，再自动删除对应的label
# path1 = 'F://github/yolov5-v5/runs/detect/detect-clothes-hat-221-0.5-test/labels/'
# path1 = 'F://github/mAP-clothes-hat/input/ground-truth/'
path1 = 'F://test/delete-image-and-label/label/'


# path2 = 'F://github/yolov5-v5/runs/detect/detect-clothes-hat-221-0.5-test/image/'
# path2 = 'F://github/mAP-clothes-hat/input/images-optional/'
path2 = 'F://test/delete-image-and-label/image/'



def file_name(file_dir1,file_dir2):
    jpg_list = []
    xml_list = []
    for root, dirs, files in os.walk(file_dir1):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                jpg_list.append(os.path.splitext(file)[0])

    for root, dirs, files in os.walk(file_dir2):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                xml_list.append(os.path.splitext(file)[0])
    diff = set(xml_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
    print(len(diff))  # 0 在jpg中，不在xml中为0个,jpg多的

    for name in diff:
        print("no xml", name + ".jpg")
        path = path2 + str(name) + '.jpg'
        print("path:", path)
        os.remove(path)

    diff2 = set(jpg_list).difference(set(xml_list))  # 差集，在b中但不在a中的元素
    print(len(diff2))  # 7 在xml中，不在jpg中为0个，xml多的
    for name in diff2:
        print("no jpg", name + ".xml")
        path = path1 + str(name) + '.xml'
        print("path:", path)
        os.remove(path)
    return jpg_list, xml_list

    # 其中os.path.splitext()函数将路径拆分为文件名+扩展名

if __name__ == '__main__':

    file_name(path1, path2)
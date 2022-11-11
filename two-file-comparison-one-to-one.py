import os

# 两个文件名称比较
# path1 = 'F://github/yolov5-v5/runs/detect/detect-clothes-hat-221-0.5-test/labels/'
# path1 = 'F://github/mAP-clothes-hat/input/ground-truth/'
path1 = 'F://test/make label/12-fire-smoke-white-black-merge/label/'


# path2 = 'F://github/yolov5-v5/runs/detect/detect-clothes-hat-221-0.5-test/image/'
# path2 = 'F://github/mAP-clothes-hat/input/images-optional/'
path2 = 'F://test/make label/12-fire-smoke-white-black-merge/image/'


def file_name(file_dir1,file_dir2):
    same = 0
    diff = 0
    jpg_list = []
    xml_list = []
    for root, dirs, files in os.walk(file_dir1):
        for file in files:
            if ((os.path.splitext(file)[1] == '.txt') | (os.path.splitext(file)[1] == '.xml')):
                jpg_list.append(os.path.splitext(file)[0])
    print("len(jpg_list): ", len(jpg_list))

    for root, dirs, files in os.walk(file_dir2):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                xml_list.append(os.path.splitext(file)[0])
    print("len(xml_list): ", len(xml_list))

    # diff = set(xml_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
    # print(len(diff))
    # for name in diff:
    #     print("no txt", name + ".jpg")

    for i in range(len(jpg_list)):
        if (jpg_list[i] == xml_list[i]):
            same = same + 1
        else:
            diff = diff + 1
            print("diff: ", i)
            print("jpg_list[i]:", jpg_list[i])


    diff2 = set(jpg_list).difference(set(xml_list))  # 差集，在b中但不在a中的元素
    print("len(diff2)", len(diff2))
    for name in diff2:
        print("no jpg", name + ".txt")

    diff = set(xml_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
    print("len(diff)", len(diff))
    for name in diff:
        print("no txt", name + ".jpg")

    return jpg_list, xml_list

    # 其中os.path.splitext()函数将路径拆分为文件名+扩展名

if __name__ == '__main__':

    file_name(path1, path2)
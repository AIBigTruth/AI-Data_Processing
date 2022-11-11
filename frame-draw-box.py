import random
import cv2

# 手动图片画框
'''无论是视频还是图片（视频帧）保存的地址后面都要加格式， 即视频的话就是.avi，.mp4等 图片就是.jpg, .png等'''
original_video_path = 'F://test/video/fall2.mp4'
new_video_path = 'F://test/video/demo-fall.avi'
# new_images_path = './data/images/child_{}.jpg'

'''假设这是预测结果'''
'''box=[左上角x, 左上角y， 右下角x, 右下角y, 置信度， 类别]'''


'''画框所需的颜色'''
# color = [random.randint(0, 255) for _ in range(3)]



def new_video(path):

    cap = cv2.VideoCapture(path)

    fps = cap.get(cv2.CAP_PROP_FPS)

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (w, h)

    avi_write = cv2.VideoWriter(new_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    # label = '{} {}'.format(box[-1], box[-2])
    # label = 'fall   87%'

    num = 0

    i = 0  # i是 0 -> nframes-1

    while cap.isOpened():
        num = num + 1
        print("num = ", num)
        ret, img = cap.read()  # 一帧一帧读取

        # stand
        if (550 <= num <= 560):
            box = [1032, 223, 1084, 311, '84%', 'stand']
        elif (561 <= num <= 570 ):
            box = [1031, 227, 1088, 313, '89%', 'stand']
        elif (571 <= num <= 580 ):
            box = [1034, 222, 1083, 314, '90%', 'stand']
        elif (581 <= num <= 590 ):
            box = [1033, 221, 1080, 312, '92%', 'stand']

        elif (591 <= num <= 600 ):
            box = [1042, 216, 1086, 313, '85%', 'stand']
        elif (601 <= num <= 610):
            box = [1043, 213, 1084, 312, '91%', 'stand']
        elif (611 <= num <= 620 ):
            box = [1042, 213, 1080, 312, '89%', 'stand']

        elif (621 <= num <= 630 ):
            box = [1054, 212, 1093, 314, '92%', 'stand']
        elif (631 <= num <= 650 ):
            box = [1052, 215, 1095, 311, '93%', 'stand']

        elif (651 <= num <= 670):
            box = [1062, 211, 1102, 312, '90%', 'stand']
        elif (671 <= num <= 690):
            box = [1063, 214, 1105, 315, '94%', 'stand']
        elif (691 <= num <= 710):
            box = [1062, 215, 1106, 313, '87%', 'stand']
        elif (711 <= num <= 720):
            box = [1061, 237, 1104, 313, '85%', 'stand']
        elif (721 <= num <= 730):
            box = [1051, 242, 1106, 315, '89%', 'stand']
        elif (731 <= num <= 749):
            box = [1060, 240, 1100, 310, '86%', 'stand']

        # fall
        elif (750 <= num <= 760 ):
            box = [1030, 270, 1100, 310, '84%', 'fall']
        elif (761 <= num <= 770):
            box = [1035, 274, 1108, 313, '89%', 'fall']
        elif (771 <= num <= 780):
            box = [1031, 272, 1102, 312, '92%', 'fall']
        elif (781 <= num <= 790):
            box = [1029, 268, 1104, 314, '87%', 'fall']
        elif (791 <= num <= 810):
            box = [1034, 274, 1102, 317, '90%', 'fall']
        elif (811 <= num <= 820):
            box = [1031, 270, 1107, 319, '96%', 'fall']
        elif (821 <= num <= 830):
            box = [1033, 273, 1103, 313, '97%', 'fall']
        elif (831 <= num <= 840):
            box = [1035, 272, 1101, 316, '92%', 'fall']
        elif (841 <= num <= 850):
            box = [1028, 268, 1098, 307, '94%', 'fall']
        elif (851 <= num <= 860):
            box = [1029, 267, 1097, 309, '90%', 'fall']
        elif (861 <= num <= 870):
            box = [1034, 272, 1108, 317, '93%', 'fall']
        elif (871 <= num <= 880):
            box = [1035, 273, 1102, 312, '93%', 'fall']
        elif (881 <= num <= 890):
            box = [1037, 275, 1104, 313, '90%', 'fall']
        elif (891 <= num <= 910):
            box = [1032, 273, 1104, 315, '82%', 'fall']
        elif (911 <= num <= 920):
            box = [1035, 278, 1104, 313, '92%', 'fall']
        elif (921 <= num <= 925):
            box = [1033, 275, 1105, 315, '88%', 'fall']
        elif (926 <= num <= 930):
            box = [1038, 278, 1106, 313, '86%', 'fall']

        # stand
        elif (931 <= num <= 940 ):
            box = [1055, 252, 1101, 313, '88%', 'stand']
        elif (941 <= num <= 950 ):
            box = [1052, 256, 1103, 312, '92%', 'stand']

        elif (951 <= num <= 960 ):
            box = [1042, 245, 1097, 302, '90%', 'stand']
        elif (961 <= num <= 970 ):
            box = [1042, 241, 1095, 300, '91%', 'stand']
        elif (971 <= num <= 980):
            box = [1040, 243, 1094, 301, '96%', 'stand']
        elif (981 <= num <= 990 ):
            box = [1041, 246, 1093, 303, '95%', 'stand']

        elif (991 <= num <= 1000 ):
            box = [1042, 241, 1093, 303, '92%', 'stand']
        elif (1001 <= num <= 1010 ):
            box = [1043, 245, 1092, 303, '89%', 'stand']
        elif (1011 <= num <= 1030):
            box = [1040, 245, 1092, 301, '87%', 'stand']
        elif (1031 <= num <= 1050):
            box = [1042, 247, 1093, 305, '90%', 'stand']
        elif (1051 <= num <= 1070):
            box = [1046, 244, 1092, 301, '91%', 'stand']
        elif (1071 <= num <= 1090):
            box = [1039, 238, 1087, 301, '87%', 'stand']
        elif (1091 <= num <= 1100):
            box = [1042, 241, 1093, 303, '92%', 'stand']
        elif (1101 <= num <= 1120):
            box = [1043, 240, 1093, 300, '87%', 'stand']
        elif (1121 <= num <= 1140):
            box = [1046, 241, 1095, 302, '89%', 'stand']
        elif (1141 <= num <= 1150):
            box = [1047, 248, 1094, 302, '90%', 'stand']

        elif (1151 <= num <= 1160):
            box = [1030, 232, 1095, 304, '94%', 'stand']
        elif (1161 <= num <= 1170):
            box = [1031, 214, 1091, 300, '91%', 'stand']
        elif (1171 <= num <= 1180):
            box = [1032, 212, 1093, 304, '93%', 'stand']

        elif (1181 <= num <= 1190):
            box = [1031, 213, 1096, 304, '90%', 'stand']


        else:
            box = [0, 0, 0, 0, '.', '.']


        if ret:

            fontscale = 2  # 字体大小
            '''框的左上角和右下角坐标'''
            c1, c2 = (box[0], box[1]), (box[2], box[3])
            if (750 <= num <= 930):
                cv2.rectangle(img, c1, c2, [0, 0, 255], fontscale, cv2.LINE_AA)  # fall 红色
                label = '{} {}'.format(box[-1], box[-2])
                if label:
                    font_thickness = max(fontscale - 1, 1)  # 字体粗度
                    '''  获取文字的(宽，高) 0是第一个字体'''
                    t_size = cv2.getTextSize(label, 0, fontScale=fontscale / 3, thickness=font_thickness)[0]
                    '''放标签的框的左上角'''
                    c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
                    # ''' -1是填充满 filled，画出放标签的框 并填充'''
                    cv2.rectangle(img, c1, c2, [0, 0, 255], -1, cv2.LINE_AA)

                    '''图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细'''
                    cv2.putText(img, label, (c1[0], c1[1] - 2), 0, fontscale / 3, [225, 255, 255], font_thickness,
                                lineType=cv2.LINE_AA)
            else:
                cv2.rectangle(img, c1, c2, [0, 255, 0], fontscale, cv2.LINE_AA)  # stand 绿色
                label = '{} {}'.format(box[-1], box[-2])
                if label:
                    font_thickness = max(fontscale - 1, 1)  # 字体粗度
                    '''  获取文字的(宽，高) 0是第一个字体'''
                    t_size = cv2.getTextSize(label, 0, fontScale=fontscale / 3, thickness=font_thickness)[0]
                    '''放标签的框的左上角'''
                    c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
                    # ''' -1是填充满 filled，画出放标签的框 并填充'''
                    cv2.rectangle(img, c1, c2, [0, 255, 0], -1, cv2.LINE_AA)

                    '''图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细'''
                    cv2.putText(img, label, (c1[0], c1[1] - 2), 0, fontscale / 3, [225, 255, 255], font_thickness,
                                lineType=cv2.LINE_AA)


            '''写入'''
            #cv2.imwrite(new_images_path.format(i), img)

            avi_write.write(img)



        else:
            break
        i += 1
    cap.release()
    avi_write.release()


new_video(original_video_path)




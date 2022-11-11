# -*- coding:utf8 -*-
import cv2
import os
import time
import sys
# 保存图片的路径
video_path = 'F://test/video/clothes-1'
savedpath = 'F://test/video/clothes-1-image'
video_list = os.listdir(video_path)

# 保存图片的帧率间隔
count = 25
i = 0   # 帧号
j = 0   # 保存的图片数量

for index, video_name in enumerate(video_list):
    video_path_ = os.path.join(video_path, video_name)
    # 开始读视频
    videoCapture = cv2.VideoCapture(video_path_)
    print("正在处理第{}个视频，总共{}个视频".format(index+1, len(video_list)))

    while True:
        success, frame = videoCapture.read()

        i += 1
        if (i % count == 0):
            # 保存图片
            j += 1

            localtime = time.time()  # 获取当前时间
            time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

            savedname = str(time1)+'-'+str(localtime) + '.jpg'
            cv2.imwrite(os.path.join(savedpath, savedname), frame)
            print('image of %s is saved' % (savedname))

        if not success:
            print('video is all read')
            break
    videoCapture.release()
    time.sleep(5)

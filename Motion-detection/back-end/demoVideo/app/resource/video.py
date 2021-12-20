from flask_restful import Resource
from flask import json, Response, send_file
import imagezmq
import cv2
import datetime
import numpy as np
import io

class Video(Resource):
    #如果方法为get 调用该方法
    def get(self):
        print("get")
        imagehub = imagezmq.ImageHub()
        print('get imagezmq')

        text = "No Target"
        background = None  # 初始化背景

        timeIndex = 1
        while(True):
            print('in circulation')
            rpi_name, jpg_buffer = imagehub.recv_jpg()
            #np.frombuffer将缓冲区变成一维数组;imdecode读取数据解码成图像格式
            image = cv2.imdecode(np.frombuffer(jpg_buffer, dtype='uint8'), -1)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (21, 21), 0)  # 括号内值越高越模糊，不能为偶数
            # 将第一帧设置为整个输入的背景
            if background is None:
                background = gray
                imagehub.send_reply(b'OK')
                continue

            if timeIndex % 20 == 0:
                background = gray
            # 当前帧和第一帧的不同它可以把两幅图的差的绝对值输出到另一幅图上面来
            frameDelta = cv2.absdiff(background, gray)
            # 二值化
            thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
            # 腐蚀膨胀
            thresh = cv2.dilate(thresh, None, iterations=2)
            # 取轮廓
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)[-2]
            # 遍历轮廓
            for c in cnts:
                if cv2.contourArea(c) < 1800:  # 对于较小矩形区域，选择忽略
                    continue
                flat = 1  # 设置一个标签，当有运动的时候为1
                # 计算轮廓的边界框，在当前帧中画出该框
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                text = "Find Target! save as D:\CCTVlook"
                # print("Find Target!")
            cv2.putText(image, text, (10, 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(image, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                        (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            bs = cv2.imencode(".jpg",image)[1].tobytes()
            print('resp done')
            imagehub.send_reply(b'OK')
            timeIndex += 1

            return Response(bs, mimetype='image/jpeg')

    def post(self):
        print("post")
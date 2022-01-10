from flask_restful import Resource
from flask import Response
import os
import cv2


picturecounter = 1  # 防止过多记录的标识

class Video(Resource):

    #如果方法为get 调用该方法
    def get(self):
        global picturecounter

        # 获取指针并赋值
        #path = r'C:\Users\Y\Desktop\project\realtime'
        path = r'/root/video/realtime'
        picnames = []
        for filenames in os.walk(path):
            picnames = filenames
            print(picnames)

        pointer = int(((picnames[2])[0].split('.'))[0])
        picturecounter = pointer

        #picpath = r'C:\Users\Y\Desktop\project\realtime\%s.jpg' % (picturecounter)
        picpath = r'/root/video/realtime/%s.jpg' % (picturecounter)

        image = cv2.imread(picpath)

        bs = cv2.imencode(".jpg", image)[1].tobytes()
        picturecounter += 1
        if(picturecounter > 5):
            picturecounter = 1

        return Response(bs, mimetype='image/jpeg')


    def post(self):
        print("post")
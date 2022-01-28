from flask_restful import Resource
from flask import Response
import os
import cv2


picturecounter = 1  # 防止过多记录的标识

class Video(Resource):

    #如果方法为get 调用该方法
    def get(self):
        global picturecounter

        # username = (request.get_json())['username']
        # db = pymysql.connect("rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com", "team", "Aaa5225975", "pidata")
        # cursor = db.cursor()
        #
        # sql = "select rpiname from user where username=\'" + username + "\'"  # 可能存在类型问题
        # cursor.execute(sql)
        # row = cursor.fetchone()
        #
        # if not row:
        #     rpiname = None
        # rpiname = str(row[0])

        #覆盖取值
        rpiname = 'raspberrypi'

        # 获取指针并赋值
        path = r'/root/video/realtime/%s' % (rpiname)
        picnames = []
        for filenames in os.walk(path):
            picnames = filenames
            print(picnames)

        pointer = int(((picnames[2])[0].split('.'))[0])
        picturecounter = pointer

        picpath = r'/root/video/realtime/%s/%s.jpg' % (rpiname, picturecounter)

        image = cv2.imread(picpath)

        bs = cv2.imencode(".jpg", image)[1].tobytes()
        picturecounter += 1
        if(picturecounter > 5):
            picturecounter = 1

        return Response(bs, mimetype='image/jpeg')

    def post(self):
        print("post")
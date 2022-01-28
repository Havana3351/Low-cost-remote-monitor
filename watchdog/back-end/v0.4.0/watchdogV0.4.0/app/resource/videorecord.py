from flask_restful import Resource, request
from flask import Response, make_response
import cv2
import pymysql

picturecounter = 1


class VideoRecord(Resource):

    def get(self):
        pass

    def post(self):
        global picturecounter

        if ((request.get_json())['picturedate'] and (request.get_json())['username'] and (request.get_json())['time']):

            date = (request.get_json())['picturedate']
            temp = date.split("-")
            year = temp[0]
            day = temp[1] + temp[2]
            username = (request.get_json())['username']

            db = pymysql.connect("rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com", "team", "Aaa5225975", "pidata")
            cursor = db.cursor()

            sql = "select rpiname from user where username=\'" + username + "\'"  # 可能存在类型问题
            cursor.execute(sql)
            row = cursor.fetchone()

            if not row:
                rpiname = None
            rpiname = str(row[0])

            picpath = r'/root/video/%s/%s/%s/%s/%s.jpg' % (rpiname, year, day, (request.get_json())['time'], str(picturecounter))

            print(picpath)
            image = cv2.imread(picpath)

            picturecounter += 1
            if (picturecounter > 10):
                picturecounter = 1
                return False

            bs = cv2.imencode(".jpg", image)[1].tobytes()
            res = make_response(bs)
            res.headers["Content-Type"] = "image/png"

            return res

        else:
            print('error')
            return "error"






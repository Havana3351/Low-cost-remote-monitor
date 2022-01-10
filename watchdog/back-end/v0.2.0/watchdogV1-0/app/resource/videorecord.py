from flask_restful import Resource, request
from flask import Response, make_response
import cv2

picturecounter = 1


class VideoRecord(Resource):


    def get(self):
        pass

    def post(self):
        global picturecounter

        if (request.get_json())['picturedate']:

            date = (request.get_json())['picturedate']
            temp = date.split("-")
            year = temp[0]
            day = temp[1] + temp[2]

            picpath = r'/root/video/username/%s/%s/%s/%s.jpg' % (year, day, (request.get_json())['time'], str(picturecounter))

            print(picpath)
            image = cv2.imread(picpath)

            picturecounter += 1
            if (picturecounter > 10):
                picturecounter = 1
                flag = 10
                return flag

            bs = cv2.imencode(".jpg", image)[1].tobytes()
            res = make_response(bs)
            res.headers["Content-Type"] = "image/png"

            return res

        else:
            print('error')
            return "error"






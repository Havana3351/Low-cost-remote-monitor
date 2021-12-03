
#import os,time,sys
from flask import json, Response, send_file
import json
from app import app
import imagezmq
import cv2
import numpy as np
import io

#from app.__init__ import datatransport,getDataThread
#from app.getDataDemo import appContainer
#from app.threaddemo import DownThread

@app.route('/')
@app.route('/home')
def home():
    return ''


@app.route('/api/data')
def data():
    #Data = {}
    #Data['day'] = day
    #Data['month'] = month
    #Data['hour'] = hour
    #Data['minute'] = minute
    #information = {}
    #information['temp'] = temp
    #information['humi'] = humi
    #Data['information'] = information

    #outdata = datatransport[len(datatransport)-1]


    testdata = '{ "Temp":[{"order":"1","value":"30"}],"Humi":[{"order":"1","value":"30"}] }'

    outputdata = json.loads(testdata)
    #return json.dumps(Data, ensure_ascii=False)
    return json.dumps(outputdata, ensure_ascii=False)


@app.route('/api/video')
def video():
    print('test')
    imagehub = imagezmq.ImageHub()
    print('get imagezmq')
    while(True):
        print('in circulation')
        rpi_name, jpg_buffer = imagehub.recv_jpg()
        image = cv2.imdecode(np.frombuffer(jpg_buffer, dtype='uint8'), -1)#np.frombuffer将缓冲区变成一维数组;imdecode读取数据解码成图像格式
        bs = cv2.imencode(".jpg",image)[1].tobytes()

        #image_name, image = imagehub.recv_image()

        #resp = Response(image, mimetype="image/jpeg")
        print('resp done')
        #return resp
        imagehub.send_reply(b'OK')

        return Response(
            bs,
            mimetype='image/jpeg',
            #as_attachment=True,
            #attachment_filename='result.jpg'
        )

#import os,time,sys
from flask import json, Response, send_file
import json
from app import app
import imagezmq
import cv2
import numpy as np
import io
import time

import threading

lock = threading.Lock()

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


    testdata = '{"deviceType":"CustomCategory","iotId":"NKuwmJf8zY6diGlFiv03000100","requestId":"6","productKey":"a1LzScM0N1F","gmtCreate":1584535854987,"deviceName":"repi","items":{"Temp":{"value":40.531,"time":1584535854988},"Humi":{"value":31.846,"time":1584535854988}}}'

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

        #image_name, image = imagehub.recv_image()

        #resp = Response(image, mimetype="image/jpeg")
        print('resp done')
        #return resp
        imagehub.send_reply(b'OK')

        return send_file(
            io.BytesIO(image),
            mimetype='image/jpeg',
            #as_attachment=True,
            #attachment_filename='result.jpg'
        )

def generate():
    # grab global references to the output frame and lock variables
    global jpg_buffer, lock

    imagehub = imagezmq.ImageHub()
    print('imagehub on')
    while True:
        # wait until the lock is acquired
        print('loop on')
        with lock:
            print('lock on')
            rpi_name, jpg_buffer = imagehub.recv_jpg()
            print('buffer received')
            if jpg_buffer is None:
                continue

            image = cv2.imdecode(np.frombuffer(jpg_buffer, dtype='uint8'), -1)
            bs = cv2.imencode(".jpg",image)[1].tobytes()
            print('decode done')
            imagehub.send_reply(b'OK')
            print('message sent')
        # yield the output frame in the byte format
        yield (bs)
        print('yield showed')
        time.sleep(2)


@app.route("/api/videofeed")
def video_feed():
    return Response(generate(),
                    mimetype='image/jpeg')
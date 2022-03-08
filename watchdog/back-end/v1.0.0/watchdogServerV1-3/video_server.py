import cv2
import datetime
import numpy as np
import os
import imagezmq
from twilio.rest import Client
import copy
import pymysql

imagehub = imagezmq.ImageHub()
background = None
text = "no target"
timeIndex = 1
frequencecounter = 0  # 保存总次数
repeatavoidcounter = 0  # 防止重复保存的标识之一
picturecounter = 0  # 防止过多记录的标识
realtimecounter = 1  # 储存实时视频到文件夹的标识
messagerepeatavoidcounter = 0 # 防止发短信过于频繁
target = False # 是否存在标记，作为是否保存的标识之一
doormessage = False
movemessage = False

# Your Account SID from twilio.com/console
account_sid = "AC492a1a3283e499614391f3aa247b26be"
# Your Auth Token from twilio.com/console
auth_token  = "fda84c6698b9e0d7990f5b813a1465d7"

client = Client(account_sid, auth_token)

db = pymysql.connect("rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com", "team", "Aaa5225975", "pidata")
cursor = db.cursor()

while(True):

    # 接收来自树莓派发来的图片以及设备名
    rpi_name, jpg_buffer = imagehub.recv_jpg()
    # np.frombuffer将缓冲区变成一维数组;imdecode读取数据解码成图像格式
    image = cv2.imdecode(np.frombuffer(jpg_buffer, dtype='uint8'), -1)

    #测试用途的强制修改
    #rpi_name = '1'
    # 通过rpiname取到phonenum和username
    sql = "select phonenum from user where rpiname=\'" + rpi_name + "\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    phonenums = []

    if row:
        for rows in row:
            phonenums.append(rows[0])


    # 门检测相关
    imagefordoor = copy.deepcopy(image)
    height, width, channels = imagefordoor.shape
    mask = np.zeros((height + 2, width + 2), "uint8")

    diff = (3, 3, 3)
    start_pixel = (25, 30)  # 取样点

    retval, _, _, rect = cv2.floodFill(imagefordoor, mask, start_pixel, (0,255,0), diff, diff)

    if retval < 5725425:  # 判定条件，面积大小
        doormessage = True   # 发出警报

    #运动检测部分
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)  # 括号内值越高越模糊，不能为偶数
    # 将第一帧设置为整个输入的背景
    if background is None:
        background = gray
        imagehub.send_reply(b'OK')
        #path = r'C:\Users\Y\Desktop\project\realtime\%s'% (rpi_name)
        path = r'/root/video/realtime/%s'% (rpi_name)
        if not os.path.exists(path):
            os.makedirs(path)

        #指针文件的删除
        if(realtimecounter == 1):
            removepointer = 5
        else:
            removepointer = realtimecounter - 1
        #removepath = r'C:\Users\Y\Desktop\project\realtime\%s\0%s.jpg' % (rpi_name, removepointer)
        removepath = r'/root/video/realtime/%s/0%s.jpg' % (rpi_name, removepointer)
        if os.path.exists(removepath):
            os.remove(removepath)

        #指针文件的添加
        #pointerpath = r'C:\Users\Y\Desktop\project\realtime\%s\0%s.jpg' % (rpi_name, realtimecounter)
        pointerpath = r'/root/video/realtime/%s/0%s.jpg' % (rpi_name, realtimecounter)
        cv2.imwrite(pointerpath, image)

        #picpath = r'C:\Users\Y\Desktop\project\realtime\%s\%s.jpg' % (rpi_name, realtimecounter)
        picpath = r'/root/video/realtime/%s/%s.jpg' % (rpi_name, realtimecounter)
        cv2.imwrite(picpath, image)

        repeatavoidcounter += 1
        messagerepeatavoidcounter += 1
        timeIndex += 1
        realtimecounter += 1#出错了
        #缓存图片数量限制
        if(realtimecounter > 5):
            realtimecounter = 1
        #继续下一层循环
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
        target = True
        movemessage = True
        # print("Find Target!")

    # 实时保存部分
    #path = r'C:\Users\Y\Desktop\project\realtime'
    path = r'/root/video/realtime'
    if not os.path.exists(path):
        os.makedirs(path)

    # 指针文件的删除
    if (realtimecounter == 1):
        removepointer = 5
    else:
        removepointer = realtimecounter - 1
    removepath = r'/root/video/realtime/%s/0%s.jpg' % (rpi_name, removepointer)
    if os.path.exists(removepath):
        os.remove(removepath)

    # 指针文件
    pointerpath = r'/root/video/realtime/%s/0%s.jpg' % (rpi_name, realtimecounter)
    cv2.imwrite(pointerpath, image)

    picpath = r'/root/video/realtime/%s/%s.jpg' % (rpi_name, realtimecounter)
    cv2.imwrite(picpath, image)
    realtimecounter += 1
    # 缓存图片数量限制
    if (realtimecounter > 5):
        realtimecounter = 1

    #短信处理
    if(messagerepeatavoidcounter >= 350):
        for phonenum in phonenums:
            if(movemessage):
                print("家里有人")
                print(phonenum)
                movemessage = False
                messagerepeatavoidcounter = 0
                #发送短信
                 message = client.messages.create(
                    to=phonenum,
                    from_="+12029492612",
                    body="你家有人"
                )

            elif(doormessage):
                print("门未关闭")
                doormessage = False
                messagerepeatavoidcounter = 0
                #发送短信
                message = client.messages.create(
                    to=phonenum,
                    from_="+12029492612",
                    body="你门没关"
                )

    # 找到目标
    if (target):

        # 保存冷却完毕
        target = False
        repeatstr = '%d' % repeatavoidcounter
        picturestr = '%d' % picturecounter
        frequencestr = '%d' % frequencecounter
        #防止过多保存，修改下面的if
        if (repeatavoidcounter > 50):

            year = datetime.datetime.now().strftime("%Y")
            day = datetime.datetime.now().strftime("%m%d")
            minute = datetime.datetime.now().strftime("%H%M")

            if (picturecounter < 10):

                picturecounter += 1

                # 画出运动检测的框
                # 遍历轮廓
                for c in cnts:
                    if cv2.contourArea(c) < 1800:  # 对于较小矩形区域，选择忽略
                        continue
                    flat = 1  # 设置一个标签，当有运动的时候为1
                    # 计算轮廓的边界框，在当前帧中画出该框
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    text = "Find target!"
                cv2.putText(image, text, (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.putText(image, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

                # 需被创建的保存路径
                path = r'/root/video/%s/%s/%s/%s' % (rpi_name, year, day, minute)

                # 保存
                if not os.path.exists(path):
                    os.makedirs(path)
                print('unchanged:' + path)
                # 图片路径
                picpath = r'/root/video/%s/%s/%s/%s/%s.jpg' % (rpi_name, year, day, minute, picturecounter)
                cv2.imwrite(picpath, image)
                print(picpath)
            else:
                repeatavoidcounter = 0
                picturecounter = 0
                frequencecounter += 1

    imagehub.send_reply(b'OK')
    messagerepeatavoidcounter += 1
    repeatavoidcounter += 1
    timeIndex += 1




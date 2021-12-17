import sys

import socket
import time
import cv2
from imutils. video import VideoStream
import imagezma

# use either of the formats below to specifiy address of display computer
# sender = imagezmq. ImageSender (connect to='tp: //192.168.1.190:5555'1
sender = imagezmq. ImageSender (connect to='tcp: /x.x.x.x:xxxx)

rpi name = socket.gethostname ( ) # send RPi hostname with each image
picam = VideoStream(usePiCamera=True) .start ()
time.sleep(2.0) # allow camera sensor to warm up
jpeg quality = 95  # 0 to 100, higher is better quality, 95 is cv2 default

while True: #send images as stream until Ctrl-C
image = picam. read()
ret code, jpg buffer = cv2. imencode(
.ipg"
image, [int (cv2. IMWRITE JPEG QUALITY) , jpeg quality])
sender. send jpg (rpi name, jpg buffer)
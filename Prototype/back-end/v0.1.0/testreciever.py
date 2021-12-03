import sys
import cv2
import imagezmq

image_hub = imagezmq.ImageHub()
while True:  # press Ctrl-C to stop image display program
    image_name, image = image_hub.recv_image()
    cv2.imshow(image_name, image)
    cv2.waitKey(1)  # wait until a key is pressed
    image_hub.send_reply(b'OK')
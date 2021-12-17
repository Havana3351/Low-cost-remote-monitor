from sense_hat import SenseHat
import time
import datetime
from linkkit import linkkit

isConnect = False

def on_connect(session_flag, rc, userdata):
    print("on_connect:%d,rc:%d,userdata:" % (session_flag, rc))
    isConnect = True
    pass

def on_disconnect(rc, userdata):
    print("on_disconnect:rc:%d,userdata:" % rc)

def on_thing_prop_post(self, request_id, code, data, message, userdata):
    print("on_thing_prop_post request id:%s, code:%d, data:%s message:%s" %
          (request_id, code, str(data), message))

#这里的内容都需要根据自己在平台创建的相关内容进行填写
lk = linkkit.LinkKit(
    host_name="购买服务所在地域",
    product_key="生成的密钥",
    device_name="自己在平台上设置的名字",
    device_secret="这个也是平台提供")

lk.on_connect = on_connect
lk.on_disconnect = on_disconnect
lk.on_thing_prop_post = on_thing_prop_post
lk.thing_setup("tsl.json")
lk.connect_async()

while True:

#read data
    sense = SenseHat()

    humidity = sense.get_humidity()
    temperature = sense.get_temperature()

    print("Humidity:%s %%rH"% humidity)
    print("temperature:%s "% temperature)
    
    prop_data = {
            "Temp":  round(temperature, 3),
            "Humi":  round(humidity, 3)
    }
    try:
        rc, request_id = lk.thing_post_property(prop_data)
        print(rc, request_id)
    except Exception as e:
        print('发生了异常：', e)
    time.sleep(5)
        
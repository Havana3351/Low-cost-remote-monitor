from sense_hat import SenseHat
import urllib2
import json
import time
import datetime

sense = SenseHat()

humidity = sense.get_humidity()
temperature = sense.get_temperature()

print("Humidity:%s %%rH"% humidity)
print("temperature:%s "% temperature)

mytemp = '%f' %temperature
myhum = '%f' %humidity

tmp_output = open('/home/pi/data/tmp_data.txt','w')
hum_output = open('/home/pi/data/hum_data.txt','w')

tmp_output.write(mytemp)
hum_output.write(myhum)

tmp_output.close
hum_output.close
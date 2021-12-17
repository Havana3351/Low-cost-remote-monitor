import urllib
import json
import time
import datetime
 
APIKEY = '这里填写平台生成的APIKEY'
        
        
def http_put():
        file = open("/home/pi/data/tmp_data.txt")
        temperature= float(file.read())
        CurTime = datetime.datetime.now()
        url='这里填写平台给出的url'
        values={'datastreams':[{"id":"temp","datapoints":[{"at":CurTime.isoformat(),"value":temperature}]}]}
 
        print ("the time is: %s" %CurTime.isoformat() )
        print ("The upload temperature value is: %.3f" %temperature)
 
        jdata = json.dumps(values)
        print (jdata)
        request = urllib.request.Request(url, jdata)
        request.add_header('api-key', APIKEY)
        request.get_method = lambda:'POST'
        request = urllib2.request.urlopen(request)
        return request.read()
 
while True:
        time.sleep(5)
        resp = http_put()
        print ("OneNET result:\n %s" %resp)
        time.sleep(5)
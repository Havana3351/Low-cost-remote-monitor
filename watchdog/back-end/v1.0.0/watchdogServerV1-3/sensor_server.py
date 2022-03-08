#coding=utf-8
import json
import pymysql
from flask import jsonify
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from twilio.rest import Client
from threading import Timer
import time

#通知部分
# Your Account SID from twilio.com/console
account_sid = "AC492a1a3283e499614391f3aa247b26be"
# Your Auth Token from twilio.com/console
auth_token  = "fda84c6698b9e0d7990f5b813a1465d7"
tel_client = Client(account_sid, auth_token)
mes_count = 0 #退火计数 间隔60*10秒发布

def alert(telnum):
    global mes_count
    if mes_count > 0:
        mes_count -= 1
        print(mes_count)
        return 0
    mes_count = 60
    print(mes_count)
    message = tel_client.messages.create(
        to=telnum,
        from_="+12029492612",
        body="温湿度异常"
    )


#物联网部分
client = AcsClient('LTAI4FibaEMFDdTEn52ZVknq', 'cVcZycw7BYEDGYBELNFjhwdgUnDEsA', 'cn-shanghai')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('iot.cn-shanghai.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2018-01-20')
request.set_action_name('QueryDevicePropertiesData')

request.add_query_param('RegionId', "cn-shanghai")
request.add_query_param('DeviceName', "repi")
# request.add_query_param('StartTime', "1585142175744")
# request.add_query_param('EndTime', "1585142201252")
request.add_query_param('Asc', "0") #倒叙查询
# request.add_query_param('PageSize', "10")
request.add_query_param('Identifier.1', "Temp")
request.add_query_param('Identifier.2', "Humi")
request.add_query_param('ProductKey', "a1LzScM0N1F")

def print_data():
    response = client.do_action(request)
    print(str(response, encoding = 'utf-8'))

#返回一条数据
def single_data():
    start_time = int(round(time.time() * 1000))
    end_time = start_time-10000 #以10秒为间隔进行向前查询
    request.add_query_param('StartTime', str(start_time))
    request.add_query_param('EndTime', str(end_time))
    request.add_query_param('PageSize', 1) #返回结果数
    response = client.do_action(request)
    #为了使用测试数据 注释掉返回实际数据的部分
    print(str(response, encoding = 'utf-8'))
    return str(response, encoding = 'utf-8')

#数据库部分
db = pymysql.connect("rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com", "team", "Aaa5225975", "pidata")
cursor = db.cursor()

def add_single_data(username,json_data):
    sql = "insert into sensors(data,username) values('%s','%s')" \
        % (json_data,username)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    print(sql)

def add_warning_data(username,json_data):
    sql = "insert into warning(data,username) values('%s','%s')" \
        % (json_data,username)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    print(sql)

def find_username(sensor):
    sql = "select username from sensorlist where sensor=\'"+sensor+"\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if not row :
        return 0
    return str(row[0])

def get_phonenum(username):
    sql = "select phonenum from user where username=\'"+username+"\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if not row :
        return 0
    return str(row[0])

#数据处理部分
def simplify_json(json_data):
    python_data = json.loads(json_data)
    data_infos = python_data["PropertyDataInfos"]["PropertyDataInfo"]
    sensor1 = str(data_infos[0]["Identifier"])
    sensor2 = str(data_infos[1]["Identifier"])
    p = {sensor1:[{"Value":"30","Time":1}],sensor2:[{"Value":"30","Time":1}]}
    p[sensor1] = data_infos[0]["List"]["PropertyInfo"]
    p[sensor2] = data_infos[1]["List"]["PropertyInfo"]
    return json.dumps(p) #str格式返回

def func():
    print('Do')
    global mes_count
    data = simplify_json(single_data())
    #存储到表sensors中
    pydata = json.loads(data)
    username = find_username(list(pydata.keys())[0])
    add_single_data(username,data)
    #判断是否高于40°
    if int(data[21]) > 4 :
        add_warning_data(username,data)
        telnum = get_phonenum(username)
        alert(telnum)
    else:
        mes_count = 0
    global timer
    timer = Timer(10, func)
    timer.start()

func()
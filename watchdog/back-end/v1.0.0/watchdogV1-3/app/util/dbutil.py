import pymysql
import re
import json
import datetime
import numpy
from .user import User
db = pymysql.connect("rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com", "team", "Aaa5225975", "pidata")
cursor = db.cursor()

def get_history_data(username):
    sql = "select data from sensors where username=\'"+username+"\' order by id desc limit 10"
    cursor.execute(sql)
    rows = cursor.fetchall()
    data = numpy.zeros((2, 10))
    for i in range(10):
        s_data = json.loads(str(rows[i][0]))
        data[0][i] = float(list(s_data.values())[1][0]["Value"])
        data[1][i] = float(list(s_data.values())[0][0]["Value"])
    return data

def get_one_data(username):
    sql = "select data from sensors where username=\'"+username+"\' order by id desc limit 0,1"
    cursor.execute(sql)
    row = cursor.fetchone()
    data = [0,0]
    s_data = json.loads(str(row[0]))
    data[0] = float(list(s_data.values())[1][0]["Value"])
    data[1] = float(list(s_data.values())[0][0]["Value"])
    return data

def sign_in(username, password):
    print(username)
    sql = "select password from signon where username=\'"+username+"\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if not row :
        return -1 #未注册
    user = User()
    user.password_hash = str(row[0])
    if user.check_password(password) == True :
        return 1 #登陆成功
    return 0 #密码错误

def sign_up(user):
    sql = "select password from signon where username=\'"+user.username+"\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row :
        return -1 #该用户名已注册
    sql1 = "insert into signon(username, password) values('%s', '%s')" % (user.username, user.password_hash)
    sql2 = "insert into user(username, identity, phonenum, dorm, room, campus) values('%s','costumer','%s','%s','%s','%s')" \
        % (user.username, user.phonenum, user.dorm, user.room, user.campus)
    try:
        cursor.execute(sql1)
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        return -2
    return 1

def get_user(username):
    user = User()
    sql = "select * from user where username= '%s'" % username
    cursor.execute(sql)
    res = cursor.fetchall()
    if res :
        user.username = res[0][0]
        user.identity = res[0][1] 
        user.phonenum = res[0][2] 
        user.dorm = res[0][3] 
        user.room = res[0][4] 
        user.campus = res[0][5] 
        user.rpiname = res[0][6]
        return user
    return None

def get_phonenum(username):
    sql = "select phonenum from user where username=\'"+username+"\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if not row :
        return 0
    return str(row[0])

def save_vertified_code(username, code):
    sql1 = "delete from vercode where user=\'"+username+"\'"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        print('rollback1')
        return 0
    sql2 = "insert into vercode(user,code,time) values('%s', '%s','%s')"\
         % (username,code,datetime.datetime.now())
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        print('rollback2')
        return 0   
    return 1

def check_code(username, code):
    sql = "select code,time from vercode where user=\'"+username+"\'"
    cursor.execute(sql)
    row = cursor.fetchall()
    if not row :
        return 0
    if str(row[0][0])==code:
        if (datetime.datetime.now()-row[0][1]).seconds<60:
            return 1
            print('check ok')
        return 2
        print('check outdate')
    print('check fail')
    return 0


def set_pw(user):
    print(user.username+user.password_hash)
    sql = "update signon set password=\'"+user.password_hash+"\'"\
        +"where username=\'"+user.username+"\'"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print('setpw roll')
        return 0
    return 1

def get_sensors(username):
    sql = "select sensor from sensorlist where username=\'"+username+"\'"
    cursor.execute(sql)
    row = cursor.fetchall()
    if row :
        #按插入顺序 1为温度 0为湿度
        s_list=[str(row[1][0]),str(row[0][0])]
        return s_list
    s_list = ["",""]
    return s_list#没有设备

def set_sensors(username,s_list):
    sql1 = "delete from sensorlist where username=\'"+username+"\'"
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
        print('srollback1')
        return 0
    sql2 = "insert into sensorlist(username,sensor) values('%s','%s'),('%s','%s')"\
         % (username,s_list[0],username,s_list[1])
    try:
        cursor.execute(sql2)
        db.commit()
    except:
        db.rollback()
        print('srollback2')
        return 0   
    return 1

def set_user(user):
    sql = "update user set phonenum='%s',dorm='%s',room='%s',campus='%s',rpiname='%s' where username='%s'"\
        % (user.phonenum,user.dorm,user.room,user.campus,user.rpiname,user.username)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        return 0
    return 1
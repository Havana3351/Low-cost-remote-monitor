import pymysql
import re
from .user import User
db = pymysql.connect("rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com", "team", "Aaa5225975", "pidata")
cursor = db.cursor()

def add_single_data(json_data):
    sql = "insert into sensors(data) values('%s')" % (json_data)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    print(sql)

def add_warning_data(json_data):
    sql = "insert into warning(data) values('%s')" % (json_data)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    print(sql)

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
    sql = "select * from user where username= %s" % username
    cursor.execute(sql)
    res = cursor.fetchall()
    if res :
        user.username = res.row[0]
        user.identity = res.row[1] 
        user.phonenum = res.row[2] 
        user.dorm = res.row[3] 
        user.room = res.row[4] 
        user.campus = res.row[5] 
        return user
    return None

def get_phonenum(username):
    sql = "select phonenum from user where username=\'"+username+"\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if not row :
        return 0
    return str(row[0])

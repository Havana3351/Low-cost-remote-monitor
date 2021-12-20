import pymysql

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
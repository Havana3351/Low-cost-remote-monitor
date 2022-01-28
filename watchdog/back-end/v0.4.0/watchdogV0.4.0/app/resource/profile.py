from flask import jsonify
from flask_restful import Resource, request
from ..util.user import User
from ..util.dbutil import get_user,get_sensors,set_sensors,set_user
import json

class Profile(Resource):
    def get(self):
        #前端使用params传值
        username = request.args.get("username")
        print(str(username)+'查看个人页面')
        user = get_user(username)
        sensors = get_sensors(username)
        data = {"name":{"information":"用户名:","content":user.username},\
            "phone":{"information":"电话号码:","content":user.phonenum},\
            "dorm":{"information":"宿舍楼:","content":user.dorm},\
            "room":{"information":"寝室号:","content":user.room},\
            "campus":{"information":"校区:","content":user.campus},\
            "temp":{"information":"温度源:","content":sensors[0]},\
            "humi":{"information":"湿度源:","content":sensors[1]},\
            "video":{"information":"视频源:","content":user.rpiname}}
        print(json.dumps(data))
        #return json.dumps(data)
        return jsonify(data)

    def post(self):
        data = request.get_json()
        if data["username"]:
            user = User()
            user.username = data["username"]
            user.phonenum = data["phonenum"]
            user.dorm = data["dorm"]
            user.room = data["room"]
            user.campus = data["campus"]
            user.rpiname = data["video"]
            s_list=[data["temp"],data["humi"]]
            if set_user(user):
                if set_sensors(user.username,s_list):
                    return 1 #成功
                return -1 #修改传感器失败
            return -2 #修改用户失败

            



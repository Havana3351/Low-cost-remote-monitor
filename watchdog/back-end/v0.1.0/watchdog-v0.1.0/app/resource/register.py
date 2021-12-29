from flask import jsonify
from flask_restful import Resource, request
from ..util.dbutil import sign_up, get_phonenum
from ..util.user import User
import json

class Register(Resource):
    def get(self):
        pass

    def post(self):
        print(request.form.get('username'))
        #处理登录请求
        if request.form.get('username') and request.form.get('password') :
            user = User()
            data = request.form.to_dict()
            user.username = data.get("username")
            user.set_password(data.get("password"))
            user.phonenum = data.get("phonenum")
            user.dorm = data.get("dorm")
            user.room = data.get("room")
            print("register:"+user.username+user.password_hash)
            res = sign_up(user)
            print("res:"+str(res))
            return res
        #处理用户名查重请求
        if request.form.get('username') :
            if get_phonenum(request.form.get('username')) != 0 :
                return -1
        print("error")
        return "error"
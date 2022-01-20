from flask import jsonify
from flask_restful import Resource, request
from ..util.user import User
from ..util.dbutil import get_user

class Profile(Resource):
    def get(self):
        username = request.args.get("username")
        user = get_user(username)
        # data = {'pe':user.username,'phonenum':user.phonenum,\
        # 'dorm':user.dorm,'room':user.room,'campus':user.campus}
        data = {}
        data['tables'] = [{"imformation": '用户名', "content": user.username},
                          {"imformation": '电话号码', "content": user.phonenum},
                          {"imformation": '所属单位', "content": user.campus},
                          {"imformation": '宿舍楼号', "content": user.dorm},
                          {"imformation": '宿舍号', "content": user.room}]

        return jsonify(data)

    # def post(self):
    #     if request:
    #         if request.form.get('username'):
    #             user = User()
    #             data = request.form.to_dict()
    #             user.username = data.get("username")
    #             user.phonenum = data.get("phonenum")
    #             user.dorm = data.get("dorm")
    #             user.room = data.get("room")
    #             user.campus = data.get('campus')
    #             if request.form.get('password'):
    #                 user.set_password(data.get('password'))
    #                 reset_password(user)


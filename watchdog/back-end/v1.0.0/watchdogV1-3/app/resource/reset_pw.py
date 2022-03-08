from flask_restful import Resource, request
from ..util.user import User
from ..util.dbutil import get_user,save_vertified_code,check_code,set_pw,get_phonenum
from ..util.random_code import ver_code
from ..util.sendmsg import send

class ResetPW(Resource):
    def get(self):
        pass

    def post(self):
        if request.form.get('vertify_code'):
            print('into 1')
            data = request.form.to_dict()
            username = data.get("username")
            code = data.get("vertify_code")
            if check_code(username, code)==1:
                user = User()
                data = request.form.to_dict()
                user.username = data.get("username")
                user.set_password(data.get("password"))
                set_pw(user)
                return 1
            if check_code(username, code)==0:
                return 0#不正确
            if check_code(username, code)==2:
                return 2#超时
        
        if request.form.get('username') and request.form.get('vertify_code') == None:
            data = request.form.to_dict()
            username = data.get("username")
            code = str(ver_code())
            print(code)
            if save_vertified_code(username,code):
                send(get_phonenum(username),code)
                print('ok sendmsg')
                return 1
            print('not ok sendmsg')
            return 0

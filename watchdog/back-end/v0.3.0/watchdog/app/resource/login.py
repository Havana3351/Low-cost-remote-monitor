from flask_restful import Resource, request
from ..util.dbutil import sign_in
from ..util.user import User
class Login(Resource):
    def get(self):
        pass

    def post(self):
        print('userrrrrrrrrrrr'+request.form.get('username'))
        if request.form.get('username') and request.form.get('password'):
            user = User()
            data = request.form.to_dict()
            username = data.get("username")
            password = data.get("password")
            res = sign_in(username, password)
            print("res:"+str(res))
            return res
        else :
            print("error")
            return "error"
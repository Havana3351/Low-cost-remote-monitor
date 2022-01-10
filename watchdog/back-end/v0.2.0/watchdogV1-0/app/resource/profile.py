from flask import jsonify
from flask_restful import Resource, request
from ..util.user import User
from ..util.dbutil import get_user

class Profile(Resource):
    def get(self):
        username = request.args.get("username")
        user = get_user(username)
        data = {'username':user.username,'phonenum':user.phonenum,\
        'dorm':user.dorm,'room':user.room,'campus':user.campus}
        return jsonify(data)

    def post(self):
        pass
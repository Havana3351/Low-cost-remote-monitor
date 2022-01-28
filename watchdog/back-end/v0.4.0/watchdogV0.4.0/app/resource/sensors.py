from flask_restful import Resource, request
from flask import Response, jsonify
import json
from ..util.dbutil import get_history_data

class Sensors(Resource):

    def get(self):
        username = request.args.get("username")
        h_data = get_history_data(username)
        data = {"tem":{"yAxis":0,"name":"温度","data":\
            [h_data[0][0],h_data[0][1],h_data[0][2],h_data[0][3],h_data[0][4],\
            h_data[0][5],h_data[0][6],h_data[0][7],h_data[0][8],h_data[0][9]],\
            "color":"#3f8cfa","tooptip":{"valueSuffix": " °C"}},\
            "hui":{"yAxis":1,"name":"湿度","data":\
            [h_data[1][0],h_data[1][1],h_data[1][2],h_data[1][3],h_data[1][4],\
            h_data[1][5],h_data[1][6],h_data[1][7],h_data[1][8],h_data[1][9]],\
            "color":"#fe377d","tooptip":{"valueSuffix": " %RH"}}}
        return jsonify(data)
    
    def post(self):
        pass
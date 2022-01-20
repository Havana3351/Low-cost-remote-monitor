from flask_restful import Resource
from flask import Response, jsonify
import json
#from ..util.iot import single_data
from ..util.simplify import simplify_json
from ..util.dbutil import add_single_data, add_warning_data

class Sensors(Resource):
    def get(self):
        data = simplify_json(single_data())
        #存储到表sensors中
        add_single_data(data)
        #判断是否高于40°
        if int(data[21]) > 4 :
            add_warning_data(data)
        #resp格式返回简化过的json数据
        return jsonify(data)
    
    def post(self):
        pass

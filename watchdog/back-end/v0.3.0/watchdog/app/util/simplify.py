import json
from flask import jsonify

def simplify_json(json_data):
    python_data = json.loads(json_data)
    data_infos = python_data["PropertyDataInfos"]["PropertyDataInfo"]
    p = {"Temp":[{"Value":"30","Time":1}],"Humi":[{"Value":"30","Time":1}]}
    p["Temp"] = data_infos[0]["List"]["PropertyInfo"]
    p["Humi"] = data_infos[1]["List"]["PropertyInfo"]
    return json.dumps(p) #str格式返回

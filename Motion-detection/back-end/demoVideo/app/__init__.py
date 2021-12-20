from flask import Flask
from flask_restful import Api
# from flask_cors import CORS
from app.resource.video import Video
#from app.resource.sensors import Sensors

app = Flask(__name__)
# CORS(app)

#api列表
api = Api(app)
api.add_resource(Video, '/api/video')
#api.add_resource(Sensors, '/api/sensors')

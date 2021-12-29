from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.resource.video import Video
from app.resource.sensors import Sensors
from app.resource.login import Login
from app.resource.register import Register
from app.resource.videosavedata import VideoSaveData
from app.resource.videorecord import VideoRecord

app = Flask(__name__)
CORS(app, supports_credentials=True)

#api列表
api = Api(app)
api.add_resource(Video, '/api/video')
api.add_resource(Sensors, '/api/sensors')
api.add_resource(Login, '/api/login')
api.add_resource(Register, '/api/register')
api.add_resource(VideoSaveData, '/api/videosavedata')
api.add_resource(VideoRecord, '/api/videorecord')

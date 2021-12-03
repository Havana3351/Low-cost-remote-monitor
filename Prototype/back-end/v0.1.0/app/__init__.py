from flask import Flask
#from flask_cors import CORS
#from app.getDataDemo import appContainer


app = Flask(__name__)
#datatransport = []


#appContainer.run()
#CORS(app, supports_credentials=True)



from app import routes

if __name__ == '__main__':
    app.run()

from flask import Flask
from src.config import Config
from src.extensions import db, jwt
from src.UserView import user_api
#from extensions import jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    jwt.init_app(app)
    
    app.register_blueprint(user_api, url_prefix='/api/v1/users') 
    
    @app.route('/', methods=['GET'])
    def index():
        return 'Greatt! End-point is working fine'
    return app
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt, get_jwt_identity, create_access_token
from .config import FlaskConfig as fcfg
from components.blueprints.authentication import signup, signin
from components.blueprints.personal import account
from components.blueprints.admin import database, server


def create_app():
    logging.getLogger('flask_cors').level = logging.DEBUG
    
    App = Flask(__name__)
    CORS(App)
    App.config.from_object(fcfg)
    jwt = JWTManager(App)
    
    # @App.after_request
    # def after_request(response):
    #     response.headers.add("Access-Control-Allow-Origin", "*")
    #     response.headers.add("Access-Control-Allow-Headers", "*")
    #     response.headers.add("Access-Control-Allow-Methods", "*")
    #     return response

    @App.route("/")
    def hello():
        return "<h1>Anime Recommendation System</h1>"

    # App.register_blueprint(image.bpimage, url_prefix='/image')
    # App.register_blueprint(gets.bpget, url_prefix='/gets')
    
    App.register_blueprint(database.bpdatabase, url_prefix='/admin')
    App.register_blueprint(server.bpserver, url_prefix='/admin')
    
    App.register_blueprint(signup.bpsignup, url_prefix='/auth')
    App.register_blueprint(signin.bpsignin, url_prefix='/auth')
    
    App.register_blueprint(account.bpaccount, url_prefix='/personal')
    
    return App
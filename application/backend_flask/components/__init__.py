import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt, get_jwt_identity, create_access_token
from .config import FlaskConfig as fcfg
import components.model_variables as modelvar
from components.blueprints.authentication import signup, signin
from components.blueprints.personal import account, interaction
from components.blueprints.admin import database, server
from components.blueprints.search import detail, general
from components.blueprints.utils import anime


def create_app():
    App = Flask(__name__)
    CORS(App)
    App.config.from_object(fcfg)
    jwt = JWTManager(App)

    @App.route("/")
    def hello():
        return "<h1>Anime Recommendation System</h1>"
    
    # print(type(modelvar.loaded_model))
    # print(type(modelvar.user2user_encoded))

    # App.register_blueprint(image.bpimage, url_prefix='/image')
    # App.register_blueprint(gets.bpget, url_prefix='/gets')
    
    App.register_blueprint(database.bpdatabase, url_prefix='/admin')
    App.register_blueprint(server.bpserver, url_prefix='/admin')
    
    App.register_blueprint(signup.bpsignup, url_prefix='/auth')
    App.register_blueprint(signin.bpsignin, url_prefix='/auth')
    
    App.register_blueprint(account.bpaccount, url_prefix='/personal')
    App.register_blueprint(interaction.bpinteraction, url_prefix='/personal')
    
    App.register_blueprint(detail.bpsearchdetail, url_prefix='/search')
    App.register_blueprint(general.bpsearchgeneral, url_prefix='/search')
    
    App.register_blueprint(anime.bpanimeutils, url_prefix='/utils')
    
    return App
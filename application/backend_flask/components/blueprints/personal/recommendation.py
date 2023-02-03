import os
from datetime import datetime
import numpy as np, pandas as pd
# from tensorflow.keras.models import model_from_json
import sqlalchemy.orm as sqlorm
from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs
from components.config import MODEL_PATH
from components.model_functions import extract_weights


bprecommendation = Blueprint('bprecommendation', __name__)


def account_output(message, error, info):
   return jsonify({
      "msg": message, 
      "error": error, 
      "info": info})


@bprecommendation.route('/recommend/', methods = ['GET'])
@jwt_required()
def getrecommendation():
   pass
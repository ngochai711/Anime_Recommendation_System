from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
import sqlalchemy.orm as sqlorm
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs


bpsearchdetail = Blueprint("bpsearchdetail", __name__)

def request_output(message, error, info):
   return jsonify({
      "msg": message, 
      "error": error, 
      "info": info
   })
   
from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
import sqlalchemy.orm as sqlorm
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs


bpanimeutils = Blueprint("bpanimeutils", __name__)

def request_output(message, error, info):
   return jsonify({
      "msg": message, 
      "error": error, 
      "info": info
   })
   

@bpanimeutils.route("/animerating", methods = ['GET'])
def getanimeratings():
   Session = new_Scoped_session()
   schema = dbs.AnimeRatingSchema()
   try:
      animeratings = Session.query(dbm.AnimeRating).all()
      Session.close()
      json_animeratings = {}
      for index, row in enumerate(animeratings):
         json_animeratings[index] = schema.dump(row)
      return request_output("Completed", "", json_animeratings)
   except Exception as e:
      return request_output("Incompleted", str(e), "")
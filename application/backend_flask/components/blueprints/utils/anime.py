from datetime import datetime
from flask import Flask, Blueprint, request, jsonify, send_file
import sqlalchemy.orm as sqlorm
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components.config import STORAGE_PATH
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
      json_animeratings = []
      for row in animeratings:
         json_animeratings.append(schema.dump(row))
      return request_output("Completed", "", json_animeratings)
   except Exception as e:
      return request_output("Incompleted", str(e), "")
   
   
@bpanimeutils.route('/imageanime/<id>', methods = ['GET'])
def getlogo(id):
   id = int(id)
   Session = new_Scoped_session()
   try:
      image = Session.query(dbm.ImageAnime).filter(dbm.ImageAnime.ID == id).first()
      Session.close()
      if image is None:
         return jsonify({'msg': 'Incompleted', 'error': 'Image not found'}), 404
      ext = image.Filename.split('.')[-1]
      return send_file(STORAGE_PATH + "anime/" + image.Filename, mimetype = 'image/' + ext)
   except Exception as e:
      return request_output("Incompleted", str(e), "")
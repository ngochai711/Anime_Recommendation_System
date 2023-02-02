from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
import sqlalchemy.orm as sqlorm
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs


bpsearchdetail = Blueprint("bpsearchdetail", __name__)


def signin_output(message, error, access_token):
   return jsonify({
      "msg": message, 
      "error": error, 
      "token": access_token
   })
   

@bpsearchdetail.route("/search/detail/anime/<int:id>", methods = ["GET"])
def searchdetail(id):
   Session = new_Scoped_session()
   try:
      anime = Session.query(dbm.Anime).options(
         sqlorm.joinedload(dbm.Anime.rel_AnimeInfo), 
         sqlorm.joinedload(dbm.Anime.rel_ImageAnime), 
         sqlorm.joinedload(dbm.Anime.rel_AnimeRating)
      ).get(id)
      if anime is None:
         return jsonify({"msg": "Incompleted"})
   except Exception as e:
      pass
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
   

@bpsearchdetail.route("/detail/anime/<int:id>", methods = ["GET"])
def searchdetail(id):
   Session = new_Scoped_session()
   schema_anime = dbs.AnimeSchema()
   schema_animeinfo = dbs.AnimeInfoSchema()
   try:
      anime = Session.query(dbm.Anime).options(
         sqlorm.joinedload(dbm.Anime.rel_AnimeInfo), 
         sqlorm.joinedload(dbm.Anime.rel_ImageAnime), 
         sqlorm.joinedload(dbm.Anime.rel_AnimeRating)
      ).get(id)
      Session.commit()
      if anime is None:
         return request_output("Incompleted", "Anime not found", "")
      json_anime = {}
      json_anime['anime'] = schema_anime.dump(anime)
      json_anime['animeinfo'] = schema_animeinfo.dump(anime.rel_AnimeInfo)
      return request_output("Completed", "", json_anime)
   except Exception as e:
      Session.rollback()
      return request_output("Incompleted", str(e), "")
   
   
# @bpsearchdetail.route("/detail/anime/<int:id>/similars", methods = ['GET'])
# def searchsimilars(id):
#    Session = new_Scoped_session()
#    schema_anime = dbs.AnimeSchema()
#    try:
#       anime = Session.query(dbm.Anime).get(id)
#       if anime is None:
#          return request_output("Incompleted", "Anime not found", "")
      
      
#       Session.commit()
#       return request_output("Completed", "", "")
#    except Exception as e:
#       Session.rollback()
#       return request_output("Incompleted", str(e), "")
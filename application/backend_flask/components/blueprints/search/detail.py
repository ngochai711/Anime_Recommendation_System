import json
from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
import sqlalchemy.orm as sqlorm
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs
from components.model_functions import find_similar_animes


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
   
   
@bpsearchdetail.route("/detail/anime/<int:id>/similars", methods = ['GET'])
def searchsimilars(id):
   amount = request.args.get('amount', default = 10, type = int)
   Session = new_Scoped_session()
   schema_anime = dbs.AnimeSchema()
   try:
      anime = Session.query(dbm.Anime).get(id)
      if anime is None:
         return request_output("Incompleted", "Anime not found", "")
      
      output = find_similar_animes(id, amount)
      if output[0]:
         for i, item in enumerate(output[1]):
            temp = Session.query(dbm.Anime).options(sqlorm.joinedload(dbm.Anime.rel_ImageAnime)).get(item["id"])
            item['anime'] = schema_anime.dump(temp)
         Session.commit()
         return request_output("Completed", "", output[1])
      else: 
         Session.commit()
         return request_output("Incompleted", "", output[1])
      
   except Exception as e:
      Session.rollback()
      return request_output("Incompleted", str(e), "")
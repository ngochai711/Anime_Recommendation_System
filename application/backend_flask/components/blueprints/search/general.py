from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import func
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs

bpsearchgeneral = Blueprint("bpsearchgeneral", __name__)


def request_output(message, error, info):
   return jsonify({
      "msg": message, 
      "error": error, 
      "info": info
   })


@bpsearchgeneral.route("/all", methods = ["GET"])
def searchall():
   searchstr = request.args.get('string', default = "", type = str)
   page = request.args.get('page', default = 1, type = int)
   numperpage = request.args.get('numperpage', default = 20, type = int)
   sortby = request.args.get('sortby', default = "", type = str)
   order = request.args.get('order', default = "asc", type = str)
   
   schema = dbs.AnimeSchema()
   Session = new_Scoped_session()
   try:
      if sortby == "score": query_orderby = dbm.Anime.Score
      elif sortby == "episodes": query_orderby = dbm.Anime.Episodes
      else: query_orderby = dbm.Anime.ID
      
      query_orderby = query_orderby.asc() if order == "asc" else query_orderby.desc()
      
      animes = Session.query(dbm.Anime
         ).filter(func.lower(dbm.Anime.Name).contains(func.lower(searchstr))
         ).order_by(query_orderby
         ).limit(numperpage).offset((page - 1) * numperpage)
      Session.commit()
      list_animes = []
      for row in animes:
         list_animes.append(schema.dump(row))
      return request_output("Completed", "", list_animes)
   except Exception as e:
      Session.rollback()
      return request_output("Incompleted", str(e), "")
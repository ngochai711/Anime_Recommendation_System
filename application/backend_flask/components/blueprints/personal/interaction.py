from datetime import datetime
import sqlalchemy.orm as sqlorm
from flask import Flask, Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs
from components.inserter import SaveProfileImage
from components.config import STORAGE_PATH

bpinteraction = Blueprint('bpinteraction', __name__)


def result_output(message, error, info):
   return jsonify({
      "msg": message, 
      "error": error, 
      "info": info})
   
   
@bpinteraction.route("/rating/get/all", methods = ['GET'])
@jwt_required()
def getallrating():
   current_user = get_jwt_identity()
   if current_user is None:
      return result_output("Incompleted", "Invalid token", "")
   
   schema_rating = dbs.RatingSchema()
   schema_anime = dbs.AnimeSchema()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return result_output("Incompleted", "Account not found", "")
      
      ratings = Session.query(dbm.Rating).options(sqlorm.joinedload(dbm.Rating.rel_Anime)).filter(dbm.Rating.ID_Account == current_user["ID"]).all()
      Session.commit()
      if ratings is None: 
         return result_output("Completed", "", "No rating yet")
      else: 
         json_ratings = {}
         for index, row in enumerate(ratings):
            json_ratings[index]['rating'] = schema_rating.dump(row)
            json_ratings[index]['anime'] = schema_anime.dump(row.rel_Anime)
         return result_output("Completed", "", json_ratings)
      
   except Exception as e:
      Session.close()
      return result_output("Incompleted", str(e), "")


@bpinteraction.route("/rating/get/<int:id>", methods = ['GET'])
@jwt_required()
def getrating():
   current_user = get_jwt_identity()
   if current_user is None:
      return result_output("Incompleted", "Invalid token", "")
   
   schema = dbs.RatingSchema()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return result_output("Incompleted", "Account not found", "")
      
      rating = Session.query(dbm.Rating).filter(dbm.Rating.ID_Account == current_user["ID"], dbm.Rating.ID_Anime == id).scalar()
      Session.commit()
      if rating is None: 
         return result_output("Completed", "", "No rating yet")
      else: 
         return result_output("Completed", "", schema.dump(rating))
      
   except Exception as e:
      Session.close()
      return result_output("Incompleted", str(e), "")
   
   
@bpinteraction.route("/rating/set/<int:id>", methods = ['POST'])
@jwt_required()
def setrating():
   point = request.args.get('point', default = 5, type = int)
   current_user = get_jwt_identity()
   if current_user is None:
      return result_output("Incompleted", "Invalid token", "")
   
   schema = dbs.RatingSchema()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return result_output("Incompleted", "Account not found", "")
      
      rating = Session.query(dbm.Rating).filter(dbm.Rating.ID_Account == current_user["ID"], dbm.Rating.ID_Anime == id).scalar()
      if rating is None: 
         new_rating = dbm.Rating(
            Point = point,
            ID_Account = current_user['ID'],
            ID_Anime = id
         )
         Session.add(new_rating)
         Session.commit()
         return result_output("Completed", "", f"Added new rating {point} successfully")
      else: 
         rating.Point = point
         Session.commit()
         return result_output("Completed", "", f"Rating changed to {point} successfully")
      
   except Exception as e:
      Session.rollback()
      return result_output("Incompleted", str(e), "")
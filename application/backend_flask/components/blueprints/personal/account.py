from datetime import datetime
import sqlalchemy.orm as sqlorm
from flask import Flask, Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs
from components.inserter import SaveProfileImage
from components.config import STORAGE_PATH

bpaccount = Blueprint('bpaccount', __name__)


def account_output(message, error, info):
   return jsonify({
      "msg": message, 
      "error": error, 
      "info": info})


@bpaccount.route('/me', methods = ['GET'])
@jwt_required()
def protected():
   current_user = get_jwt_identity()
   return jsonify(current_user), 200 # ok


@bpaccount.route("/info/get", methods=['GET'])
@jwt_required()
def getinfo():
   current_user = get_jwt_identity()   
   if current_user is None:
      return account_output("Incompleted", "Invalid token", "")
   
   schema = dbs.AccountInfoSchema()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return account_output("Incompleted", "Account not found", "")
      acc_info = Session.query(dbm.AccountInfo).get(acc.ID_AccountInfo)
      Session.close()
      return account_output("Completed", "", schema.dump(acc_info))
      
   except Exception as e:
      Session.close()
      return account_output("Incompleted", str(e), "")
   

@bpaccount.route("/info/set", methods=['POST', 'PUT'])
@jwt_required()
def changeinfo():
   current_user = get_jwt_identity()
   if current_user is None:
      return account_output("Incompleted", "Invalid token", "")
   
   info = request.get_json()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return account_output("Incompleted", "Account not found", "")
      else:
         acc_info = Session.query(dbm.AccountInfo).get(acc.ID_AccountInfo)
         acc_info.Name = info['name']
         acc_info.Birthdate = datetime.strptime(info['birth'], '%d/%m/%Y'), 
         acc_info.Gender = info['gender']
         Session.commit()
         return account_output("Completed", "", "")
   
   except Exception as e:
      Session.rollback()
      return account_output("Incompleted", str(e), "")
   

@bpaccount.route('/avatar/set', methods = ['POST'])
@jwt_required()
def setavatar():
   if 'file' not in request.files:
      return jsonify({"msg": "Completed", "error": "No file path", "info": ""})
   current_user = get_jwt_identity()
   if current_user is None:
      return jsonify({"msg": "Incompleted", "error": "Invalid token", "info": ""})
   
   f = request.files['file']
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).options(sqlorm.joinedload(dbm.Account.rel_AccountInfo)).get(current_user['ID'])
      if acc == None:
         Session.close()
         return jsonify({"msg": "Incompleted", "error": "Account not found", "info": ""})
      output = SaveProfileImage(Session, f)
      if output[0]: 
         acc.rel_AccountInfo.ID_ImageProfile = output[1].ID
         Session.commit()
         return jsonify({'msg': 'Completed', "error": "", "info": output[1].ID})
      else: 
         Session.rollback()
         return jsonify({'msg': 'Incompleted', "error": output[1], "info": ""})
   except Exception as e:
      Session.rollback()
      return jsonify({'msg': 'Incompleted', 'error': str(e)})
   
   
@bpaccount.route('/avatar/get', methods = ['GET'])
@jwt_required()
def getavatar():
   current_user = get_jwt_identity()
   if current_user is None:
      return jsonify({"msg": "Incompleted", "error": "Invalid token", "info": ""})

   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).options(sqlorm.joinedload(dbm.Account.rel_AccountInfo)).get(current_user['ID'])
      if acc == None:
         Session.close()
         return jsonify({"msg": "Incompleted", "error": "Account not found", "info": ""})
   
      if acc.rel_AccountInfo.ID_ImageProfile is None:
         return jsonify({"msg": "Incompleted", "error": "No avatar", "info": ""})
      
      image = Session.query(dbm.ImageProfile).get(acc.rel_AccountInfo.ID_ImageProfile)
      Session.close()
      ext = image.Filename.split('.')[-1]
      return send_file(STORAGE_PATH + "profile/" + image.Filename, mimetype = 'image/' + ext)
   
   except Exception as e:
      Session.rollback()
      return jsonify({'msg': 'Incompleted', 'error': str(e)})
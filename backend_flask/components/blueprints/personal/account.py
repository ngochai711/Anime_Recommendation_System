import json
from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs

bpaccount = Blueprint('bpaccount', __name__)


@bpaccount.route('/me', methods = ['GET'])
@jwt_required()
def protected():
   # Access the identity of the current user with get_jwt_identity
   current_user = get_jwt_identity()
   #return jsonify(logged_in_as=current_user), 200 # ok
   return jsonify(current_user)#, 200 # ok


@bpaccount.route("/getinfo", methods=['GET'])
@jwt_required()
def getinfo():
   current_user = get_jwt_identity()   
   if current_user is None:
      return jsonify({"msg": "Incompleted", "error": "Invalid token", "info": ""})
   
   schema = dbs.AccountInfoSchema()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return jsonify({"msg": "Incompleted", "error": "Account not found", "info": ""})
      acc_info = Session.query(dbm.AccountInfo).get(acc.ID_AccountInfo)
      Session.close()
      return jsonify({"msg": "Completed", "error": "", "info": schema.dump(acc_info)})
      
   except Exception as e:
      Session.close()
      return jsonify({"msg": "Incompleted", "error": str(e), "info": ""})
   

@bpaccount.route("/setinfo", methods=['POST', 'PUT'])
@jwt_required()
def changeinfo():
   current_user = get_jwt_identity()
   if current_user is None:
      return jsonify({"msg": "Incompleted", "error": "Invalid token"})
   
   schema = dbs.AccountInfoSchema()
   info = request.get_json()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return jsonify({"msg": "Incompleted", "error": "Account not found", "info": ""})
      else:
         acc_info = Session.query(dbm.AccountInfo).get(acc.ID_AccountInfo)
         acc_info.Name = info['name']
         acc_info.Birthdate = datetime.strptime(info['birth'], '%m/%d/%Y'), 
         acc_info.Gender = info['gender']
         acc_info.Phone_number = info['phone']
         acc_info.Identification_number = info['idt']
         Session.commit()
         return jsonify({"msg": "Completed", "error": ""})
   
   except Exception as e:
      Session.rollback()
      return jsonify({"msg": "Incompleted", "error": str(e)})
   

@bpaccount.route("/getaddress", methods = ['GET'])
@jwt_required()
def getaddress():
   current_user = get_jwt_identity()   
   if current_user is None:
      return jsonify({"msg": "Incompleted", "error": "Invalid token", "info": ""})
   schema = dbs.AddressSchema()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return jsonify({"msg": "Incompleted", "error": "Account not found", "info": ""})
      addresses = Session.query(dbm.Address).filter(dbm.Address.ID_AccountInfo==acc.ID_AccountInfo).order_by(dbm.Address.ID.desc()).all()
      Session.commit()
      json_addresses = {}
      for index, item in enumerate(addresses):
         json_addresses[index] = schema.dump(item)
      print(json_addresses)
      return jsonify({"msg": "Completed", "error": "", "info": json_addresses})
   except Exception as e:
      Session.rollback()
      return jsonify({"msg": "Incompleted", "error": str(e)})
   

@bpaccount.route("/addaddress", methods = ['POST'])
@jwt_required()
def addaddress():
   current_user = get_jwt_identity()   
   if current_user is None:
      return jsonify({"msg": "Incompleted", "error": "Invalid token", "info": ""})
   info = request.get_json()
   schema = dbs.AddressSchema()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return jsonify({"msg": "Incompleted", "error": "Account not found", "info": ""})
      new_address = dbm.Address(
         Detail_address=info['detail'], 
         ID_AccountInfo=acc.ID_AccountInfo, 
         ID_City=info['city'], 
         ID_District=info['district'], 
         ID_Ward=info['ward'])
      Session.add(new_address)
      Session.commit()
      return jsonify({"msg": "Completed", "error": "", "info": schema.dump(new_address)})
   except Exception as e:
      Session.rollback()
      return jsonify({"msg": "Incompleted", "error": str(e)})
   

@bpaccount.route("/deladdress/<int:id>", methods = ['DELETE'])
@jwt_required()
def deladdress(id):
   current_user = get_jwt_identity()   
   if current_user is None:
      return jsonify({"msg": "Incompleted", "error": "Invalid token"})
   info = request.get_json()
   Session = new_Scoped_session()
   try:
      acc = Session.query(dbm.Account).get(current_user['ID'])
      if acc == None:
         Session.close()
         return jsonify({"msg": "Incompleted", "error": "Account not found", "info": ""})
      address = Session.query(dbm.Address).get(id)
      if acc.ID_AccountInfo != address.ID_AccountInfo:
         Session.close()
         return jsonify({"msg": "Incompleted", "error": "Cannot delete other user's address"})
      Session.remove(address)
      Session.commit()
      return jsonify({"msg": "Completed", "error": ""})
   except Exception as e:
      Session.rollback()
      return jsonify({"msg": "Incompleted", "error": str(e)})
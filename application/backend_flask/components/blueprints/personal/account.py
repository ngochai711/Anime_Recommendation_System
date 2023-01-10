from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs

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


@bpaccount.route("/getinfo", methods=['GET'])
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
   

@bpaccount.route("/setinfo", methods=['POST', 'PUT'])
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
   


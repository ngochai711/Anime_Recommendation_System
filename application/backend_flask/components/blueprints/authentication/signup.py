from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs
from components.security import make_hash
from components.inserter import SaveImageFromURL, SetupAccount

bpsignup = Blueprint('bpsignup', __name__)


def signup_output(message, error, access_token):
   return jsonify({
      "msg": message, 
      "error": error, 
      "token": access_token})

   
@bpsignup.route('/signup', methods=['POST'])
def signup():
   schema = dbs.AccountSchema()
   Session = new_Scoped_session()
   try:
      email = request.json['email']
      username = request.json['username']
      phone = request.json['phone']
      
      existed_email = Session.query(dbm.Account.Email).filter(dbm.Account.Email==email, dbm.Account.Account_type==0).first()
      if (not existed_email is None):
         return signup_output("Incompleted", "Email existed", "")
      
      existed_username = Session.query(dbm.Account.Username).filter(dbm.Account.Username==username, dbm.Account.Account_type==0).first()
      if (not existed_username is None):
         return signup_output("Incompleted", "Username existed", "")

      password = make_hash(request.json['password'])
      
      output = SetupAccount(Session, email, username, password, 0, 4, username, phone)
      if output[0] == True:
         Session.commit()
         access_token = create_access_token(identity=schema.dump(output[1]))
         return signup_output("Completed", "", access_token)
      else:
         Session.rollback()
         signup_output("Incompleted", output[1], "")
   
   except Exception as e:
      Session.rollback()
      return signup_output("Incompleted", str(e), "")
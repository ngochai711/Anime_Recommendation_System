import secrets
from flask import Flask, Blueprint, request, jsonify, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components.inserter import SetupAccount
from components import dbmodels as dbm, dbschemas as dbs
from components.security import make_hash, check_hash, oauth

bpsignin = Blueprint('bpsignin', __name__)


@bpsignin.route('/me', methods = ['GET'])
@jwt_required()
def me():
   current_user = get_jwt_identity()
   return jsonify(current_user)

def signin_output(message, error, access_token):
   return jsonify({
      "msg": message, 
      "error": error, 
      "token": access_token})
   

@bpsignin.route('/signin', methods = ['POST'])
def signin():
   schema = dbs.AccountSchema()
   Session = new_Scoped_session()
   try:
      username_or_email = request.json["username_or_email"]
      password = request.json["password"]
      
      acc = Session.query(dbm.Account).filter(dbm.Account.Email==username_or_email, dbm.Account.Account_type==0).first() or \
            Session.query(dbm.Account).filter(dbm.Account.Username==username_or_email, dbm.Account.Account_type==0).first()
         
      if (acc != None):
         result = check_hash(acc.Password, password)
         if (result[0]):
            if result[1]:
               Session.get(dbm.Account).update({"Password": make_hash(password)}, synchronize_session="fetch")
            access_token = create_access_token(identity=schema.dump(acc))
            Session.commit()
            return signin_output("Completed", "", access_token)
         
      Session.close()
      return signin_output("Incompleted", "Wrong username or password", "")
      
   except Exception as e:
      Session.rollback()
      return signin_output("Incompleted", str(e), "")


@bpsignin.route('/signin/google/')
def googlesignup():
   redirect_uri = url_for('bpsignin.googleauthorize', _external=True)
   return oauth.google.authorize_redirect(redirect_uri)


@bpsignin.route('/signin/google/authorize')
def googleauthorize():
   schema = dbs.AccountSchema()
   Session = new_Scoped_session()
   try:
      token = oauth.google.authorize_access_token()
      profile = oauth.google.get('userinfo').json()
      
      name = profile["name"]
      picture_url = profile["picture"]
      email = profile["email"]
      username = "accounts.google." + profile["id"]
      
      acc = Session.query(dbm.Account).filter(dbm.Account.Email==email, dbm.Account.Account_type==1).first()
      if acc is not None:
         access_token = create_access_token(identity=schema.dump(acc))
         Session.close()
         return signin_output("Completed", "", access_token)
      
      password = make_hash(secrets.token_urlsafe(64))
      
      output = SetupAccount(Session, email, username, password, 1, 4, name, None, picture_url)
      if output[0] == True:
         Session.commit()
         access_token = create_access_token(identity=schema.dump(output[1]))
         return signin_output("Completed", "", access_token)
      else:
         Session.rollback()
         return signin_output("Incompleted", output[1], "")
      
      # new_Account = dbm.Account(Email=email, Username=username, Password=password, Account_type=1, ID_Permission=4)
      # access_token = create_access_token(identity=schema.dump(new_Account))
      # Session.add(new_Account)
      # Session.commit()
      # return signin_output("Completed", "", access_token)
      
   except Exception as e:
      Session.rollback()
      return signin_output("Incompleted", str(e), "")
    


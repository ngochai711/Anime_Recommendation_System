from flask import Flask, Blueprint, request, jsonify

import flask_jwt_extended as jwte
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs
from components.security import make_hash, check_hash

bpauth = Blueprint('bpauth', __name__)

# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@bpauth.route('/protected', methods = ['GET'])
@bpauth.route('/me', methods = ['GET'])
@jwte.jwt_required()
def protected():
   # Access the identity of the current user with get_jwt_identity
   current_user = jwte.get_jwt_identity()
   #return jsonify(logged_in_as=current_user), 200 # ok
   return jsonify(current_user)#, 200 # ok
   

@bpauth.route('/signup', methods=['POST'])
def signup():
   schema = dbs.AccountSchema()
   Session = new_Scoped_session()
   try:
      email = request.json['email']
      permission = int(request.json['permission'])
      username = request.json['username']
      password = make_hash(request.json['password'])
      
      existedEmail = Session.query(dbm.Account).filter(dbm.Account.Email == email).first()
      existedUsername = Session.query(dbm.Account).filter(dbm.Account.Username == username).first()

      if (not existedEmail is None):
         Session.close()
         return jsonify({"Error": "Email existed", "msg": "Incompleted"})#, 409
      elif (not existedUsername is None):
         Session.close()
         return jsonify({"Error": "Username existed", "msg": "Incompleted"})#, 409

      new_account = dbm.Account(Username=username, Password=password, Email=email, ID_Permission=permission)
      Session.add(new_account)
      Session.commit()
      Session.close()
      return jsonify({"msg": "Successful", "account": schema.dump(new_account)})#, 201
   
   except Exception as e:
      Session.rollback()
      Session.close()
      return jsonify({"Error": str(e), "msg": "Incompleted"})#, 409


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@bpauth.route('/signin', methods = ['POST'])
def signin():
   # username = request.json["username"]
   # password = request.json["password"]
   # if username != 'test' or password != 'test':
   #    return jsonify({"msg": "Wrong user"}), 401 # unauthorized
   # token = jwte.create_access_token(identity=username)
   # return jsonify(access_token=token)
   schema = dbs.AccountSchema()
   Session = new_Scoped_session()
   try:
      userNameOrEmail = request.json["username_or_email"]
      password = request.json["password"]
      acc = Session.query(dbm.Account).filter(dbm.Account.Email==userNameOrEmail).first()
      if (acc is None):
         acc = Session.query(dbm.Account).filter(dbm.Account.Username==userNameOrEmail).first()
         
      if (acc != None):
         
         result = check_hash(acc.Password, password)
         if (result[0]):
            if result[1]:
               Session.get(dbm.Account, acc.ID).update({"Password": make_hash(password)}, synchronize_session="fetch")
               Session.commit()
            token = jwte.create_access_token(identity=schema.dump(acc),expires_delta=False)
            Session.close()
            return jsonify({"msg": "Successful", "token": token, "uid": acc.ID})#, 200
         else: 
            # return jsonify({acc.Password: "a", "msg": "Wrong password"}), 401
            Session.close()
            return jsonify({"msg": "Wrong password"})#, 401
      else:
         Session.close()
         return jsonify({"msg": "Account not exists"})#, 401
   except Exception as e:
      Session.rollback()
      Session.close()
      return jsonify({"Error": str(e), "Status": "Incompleted"})#, 409
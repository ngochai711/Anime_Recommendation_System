from flask import Flask, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from components.security import blocklistJWT
from components.config import FlaskConfig as fcfg

bpsignout = Blueprint('bpsignout', __name__)


@bpsignout.route('/signout', methods = ['DELETE'])
@jwt_required()
def signout():
   jti = get_jwt()['jti']
   blocklistJWT.set(jti, "", ex=fcfg.JWT_ACCESS_TOKEN_EXPIRES)
   return jsonify({"msg": "Token revoked successfully"})
from datetime import datetime
from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from components.dbsettings import new_Scoped_session
from components import dbmodels as dbm, dbschemas as dbs

bpsearchgeneral = Blueprint("bpsearchgeneral", __name__)


@bpsearchgeneral.route("/search/all", methods = ["POST"])
def searchall():
   page = request.args.get('page', default = 1, type = int)
   numperpage = request.args.get('numperpage', default = 20, type = int)
   # sortby = request.args.get('sortby', default = 20, type = int)
   pass
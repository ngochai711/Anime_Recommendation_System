from flask import Blueprint, request, jsonify
from ...dbmodels import *
from ...dbschemas import *
from ...dbsettings import new_Scoped_session, Base, Engine
from ...inserter import *
import glob, os
from ...config import DB_NAME, STORAGE_PATH
import json
import platform

bpadmin = Blueprint('bpadmin', __name__)

@bpadmin.route('/serverinfo', methods = ['GET'])
def serverinfo():
    return jsonify({"system": platform.system(), "release": platform.release(), "version": platform.version()})


@bpadmin.route('/clearimages/anime', methods = ['GET','POST'])
def clearimages():
    print("Clearing images...")
    try:
        Session = new_Scoped_session()
        Session.query(ImageAnime).remove()
        return {"Images cleared"}
    except Exception as e:
        return {str(e)}


@bpadmin.route('/resetdatabase', methods = ['POST'])
def dropalltables():
    clearimages()

    print("Dropping all tables...")
    Session = new_Scoped_session()

    Session.execute("SET FOREIGN_KEY_CHECKS = 0")
    
    commands = Session.execute("SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;') FROM information_schema.tables WHERE table_schema = '" + DB_NAME + "';")

    for command in commands:
        Session.execute(command[0])

    Session.execute("SET FOREIGN_KEY_CHECKS = 1")
    Session.commit()

    print("Recreating all tables...")
    Base.metadata.create_all(Engine)

    return "Done"


# @bpadmin.route('/initdatabase/<int:index>', methods = ['POST'])
# def initdatabase(index):
#     if index==1:
#         print("Initializing database...")
#         initversions()
#         insertlocations()
#         insertpermission()
#         insertimagetype()
#     elif index==2:
#         insertvehiclesupport()
#         inserttestaccounts()
#     else: 
#         return "Index not valid"
#     return f"Done {index}"



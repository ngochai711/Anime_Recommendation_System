from flask import Blueprint, request, jsonify
from ...dbmodels import *
from ...dbsettings import new_Scoped_session, Base, Engine
from ...inserter import InsertAnimes
from ...config import DB_NAME, STORAGE_PATH

bpdatabase = Blueprint('bpdatabase', __name__)


@bpdatabase.route('database/clearimages/anime', methods = ['GET','POST'])
def clearimages():
    print("Clearing images...")
    try:
        Session = new_Scoped_session()
        Session.query(ImageAnime).remove()
        return {"Images cleared"}
    except Exception as e:
        return {str(e)}


@bpdatabase.route('/database/reset', methods = ['POST'])
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


@bpdatabase.route('/database/import', methods = ["POST"])
def importdata():
    Session = new_Scoped_session()
    output = InsertAnimes(Session)
    if output[0]:
        Session.commit()
        return "Done"
    else:
        Session.rollback()
        return f"Error: {output[1]}"
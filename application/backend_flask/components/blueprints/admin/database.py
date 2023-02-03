import json
from flask import Blueprint, request, jsonify
from ...dbmodels import *
from ...dbsettings import new_Scoped_session, Base, Engine
from ...inserter import InsertAnimes, InsertAnimeImages, TruncateTables
from ...config import DB_NAME, STORAGE_PATH
from components.imagescraper import get_original_images_custom

bpdatabase = Blueprint('bpdatabase', __name__)


@bpdatabase.route('database/clear/imageanime', methods = ["DELETE"])
def clearimages():
    print("Clearing images...")
    try:
        Session = new_Scoped_session()
        images = Session.query(ImageAnime).all()
        Session.delete(images)
        Session.commit()
        TruncateTables({"IMAGEANIME"})
        return "Images cleared"
    except Exception as e:
        return str(e)


@bpdatabase.route('/database/reset', methods = ['DELETE'])
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


@bpdatabase.route('/database/import/anime', methods = ["POST"])
def importanime():
    Session = new_Scoped_session()
    output = InsertAnimes(Session)
    if output[0]:
        Session.commit()
        return "Done"
    else:
        Session.rollback()
        return f"Error: {output[1]}"
    
    

@bpdatabase.route('/database/import/image/<int:num_per_anime>', methods = ["POST"])
def importimage(num_per_anime):
    output = InsertAnimeImages(num_per_anime)
    if output[0]:
        return "Done"
    else: return f"Error: {output[1]}"
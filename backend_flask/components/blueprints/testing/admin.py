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


@bpadmin.route('/insertvehiclesupport', methods = ['POST'])
def insertvehiclesupport():
    print("Inserting Vehicle support tables...")
    return InsertVehicleSupportTable()

@bpadmin.route('/inserttestaccounts', methods = ['POST'])
def inserttestaccounts():
    print("Inserting test accounts...")
    return InsertTestAccounts()

@bpadmin.route('/insertlocations', methods = ['POST'])
def insertlocations():
    print("Inserting locations...")
    return InsertLocation2()

@bpadmin.route('/insertpermissions', methods = ['POST'])
def insertpermission():
    print("Inserting permissions...")
    return InsertPermission()

@bpadmin.route('/insertimagetypes', methods = ['POST'])
def insertimagetype():
    print("Inserting image types...")
    return InsertImageType()

@bpadmin.route('/initversions', methods = ['POST'])
def initversions():
    Session = new_Scoped_session()
    print("Initializing version...")
    TruncateTables({"Version"})
    Session.add(Version(Name="Locations", Version=1))
    Session.add(Version(Name="Permissions", Version=1))
    Session.add(Version(Name="ImageTypes", Version=1))
    Session.commit()
    Session.close()
    return jsonify({"msg": "Success"})


@bpadmin.route('/clearimages', methods = ['GET','POST'])
def clearimages():
    print("Clearing images...")
    TruncateTables({"IMAGE"})
    posts = glob.glob(STORAGE_PATH + "post/*")
    logos = glob.glob(STORAGE_PATH + "logo/*")
    users = glob.glob(STORAGE_PATH + "user/*")
    identities = glob.glob(STORAGE_PATH + "identity/*")
    for folder in [posts, logos, users, identities]:
        for i in folder:
            os.remove(i)
    return jsonify({"msg": "Images cleared"})


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


@bpadmin.route('/initdatabase/<int:index>', methods = ['POST'])
def initdatabase(index):
    if index==1:
        print("Initializing database...")
        initversions()
        insertlocations()
        insertpermission()
        insertimagetype()
    elif index==2:
        insertvehiclesupport()
        inserttestaccounts()
    else: 
        return "Index not valid"
    return f"Done {index}"


@bpadmin.route('/test', methods = ['GET', 'POST'])
def test():
    return "Done"


from flask import Blueprint, request, jsonify
from ...dbmodels import *
from ...dbschemas import *
from ...dbsettings import new_Scoped_session, new_Session
from ...inserter import *
from ...dbschemas import *


STEP = 100
CONCURRENT = 50
bpget = Blueprint('bpget', __name__)

@bpget.route('/', methods = ['GET'])
def get_articles():
    return "Hello from gets"

@bpget.route('/isemailexists/<email>', methods = ['GET'])
def ifemailexists(email):
    Session = new_Scoped_session()
    try:
        user = Session.query(Account).filter(Account.Email == email).first()
        Session.close()
        return jsonify({"exists": not user is None})
    except Exception as e:
        Session.rollback()
        Session.close()
        return jsonify({"exists": False})

@bpget.route('/isusernameexists/<username>', methods = ['GET'])
def ifusernameexists(username):
    Session = new_Scoped_session()
    try:
        user = Session.query(Account).filter(Account.Username == username).first()
        Session.close()
        return jsonify({"exists": not user is None})
    except Exception as e:
        Session.rollback()
        Session.close()
        return jsonify({"exists": False})

@bpget.route('/isphoneexists/<phone>', methods = ['GET'])
def ifphoneexists(phone):
    Session = new_Scoped_session()
    try:
        user = Session.query(AccountInfo).filter(AccountInfo.Phone_number == phone).first()
        Session.close()
        return jsonify({"exists": not user is None})
    except Exception as e:
        Session.rollback()
        Session.close()
        return jsonify({"exists": False})

@bpget.route('/step', methods=['GET'])
def getStep():
    return jsonify(STEP)

@bpget.route('/concurrent', methods=['GET'])
def getConcurrent():
    return jsonify(CONCURRENT)

@bpget.route('/version/<name>', methods = ['GET'])
def getversions(name):
    Session = new_Scoped_session()
    try:
        schema = VersionSchema()
        print("Here: " + name)
        result = Session.query(Version).filter(Version.Name == name).first()
        print("Found: " + result.Name)
        Session.close()
        return jsonify(schema.dump(result))
    except Exception as e:
        Session.rollback()
        Session.close()
        return jsonify({"error": str(e)})

@bpget.route('/permissions', methods = ['GET'])
def getpermissions():
    with new_Session() as Session:
        try:
            schema = PermissionSchema(many=True)
            permissions = Session.query(Permission).all()
            Session.close()
            return jsonify(schema.dump(permissions))
        except Exception as e:
            Session.rollback()
            Session.close()
            return jsonify({"error": str(e)})

@bpget.route('/count/cities/', methods = ['GET'])
def countcities():
    with new_Session() as Session:
        try:
            count = Session.query(City).count()
            return jsonify(count)
        except Exception as e:
            Session.rollback()
            return jsonify({"error": str(e)})

@bpget.route('/cities/<fid>', methods = ['GET'])
def getcities(fid):
    with new_Session() as Session:
        try:
            FirstID = int(fid)
            schema = CitySchema(many=True)
            cities = Session.query(City).where(City.ID >= FirstID).limit(STEP)
            return jsonify(schema.dump(cities))
        except Exception as e:
            Session.rollback()
            return jsonify({"error": str(e)})

@bpget.route('/count/districts', methods = ['GET'])
def countdistricts():
    with new_Session() as Session:
        try:
            count = Session.query(District).count()
            return jsonify(count)
        except Exception as e:
            Session.rollback()
            return jsonify({"error": str(e)})

@bpget.route('/districts/<fid>', methods = ['GET'])
def getdistricts(fid):
    with new_Session() as Session:
        try:
            FirstID = int(fid)
            schema = DistrictSchema(many=True)
            districts = Session.query(District).where(District.ID >= FirstID).limit(STEP)
            return jsonify(schema.dump(districts))
        except Exception as e:
            Session.rollback()
            return jsonify({"error": str(e)})

@bpget.route('/count/wards', methods = ['GET'])
def countwards():
    with new_Session() as Session:
        try:
            count = Session.query(Ward).count()
            return jsonify(count)
        except Exception as e:
            Session.rollback()
            return jsonify({"error": str(e)})

@bpget.route('/wards/<fid>', methods = ['GET'])
def getwards(fid):
    with new_Session() as Session:
        try:
            firstID = int(fid)
            schema = WardSchema(many=True)
            wards = Session.query(Ward).where(Ward.ID >= firstID).limit(STEP)
            return jsonify(schema.dump(wards))
        except Exception as e:
            Session.rollback()
            return jsonify({"error": str(e)})


@bpget.route('/imagetypes', methods = ['GET'])
def getimagetypes():
    with new_Session() as Session:
        try:
            schema = ImageTypeSchema(many=True)
            imagetypes = Session.query(ImageType).all()
            return jsonify(schema.dump(imagetypes))
        except Exception as e:
            Session.rollback()
            return jsonify({"error": str(e)})
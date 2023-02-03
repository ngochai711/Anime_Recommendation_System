from flask import Blueprint, request, jsonify
from flask_cors import CORS
import platform

bpserver = Blueprint('bpserver', __name__)
CORS(bpserver)

@bpserver.route('/serverinfo', methods = ['GET'])
def serverinfo():
    return jsonify({"system": platform.system(), "release": platform.release(), "version": platform.version(), "name": platform.uname()})


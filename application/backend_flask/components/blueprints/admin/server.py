from flask import Blueprint, request, jsonify
import platform

bpserver = Blueprint('bpserver', __name__)


@bpserver.route('/serverinfo', methods = ['GET'])
def serverinfo():
    return jsonify({"system": platform.system(), "release": platform.release(), "version": platform.version(), "name": platform.uname()})


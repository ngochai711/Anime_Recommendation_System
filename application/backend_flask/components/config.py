from datetime import timedelta
from dotenv import load_dotenv
from os import environ
from argon2 import Type as ArgonType
import platform

machineinfo = platform.uname()

HOME_DIRECTORY = '/media/knguyen02311/Data Disk/DataScience/machine_learning/ML_cong_cu/Anime_Recommendation_System/application/backend_flask/' \
if machineinfo[1] == "knguyen02311-LENOVO" \
else '/var/lib/jenkins/workspace/anime-recommendation-development/application/backend_flask/'
   
STORAGE_PATH = HOME_DIRECTORY + 'storage/'

load_dotenv(dotenv_path=HOME_DIRECTORY + '.env')

DB_USERNAME = environ.get('DBUSERNAME')
DB_PASSWORD = environ.get('DBPASSWORD')
DB_NAME = environ.get('DBNAME')

class FlaskConfig:
   SECRET_KEY = environ.get('SECRET_KEY')
   JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
   JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=21)

class SQLAlchemyConfig:
   SQLALCHEMY_DATABASE_URL = "mysql://" + DB_USERNAME + ":" + DB_PASSWORD + "@localhost/" + DB_NAME + "?unix_socket=/var/run/mysqld/mysqld.sock"
   ECHO = False
   AUTO_FLUSH = True
   AUTO_COMMIT = False
   POOL_SIZE = 15
   MAX_OVERFLOW = 10
   
class SecurityConfig:
   ARGON_TIMECOST = 4
   ARGON_HASHLEN = 64
   ARGON_SALTLEN = 32
   ARGON_TYPE = ArgonType.D
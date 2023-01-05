from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import SQLAlchemyConfig as scfg

Engine = create_engine(url=scfg.SQLALCHEMY_DATABASE_URL, echo=scfg.ECHO, pool_size=scfg.POOL_SIZE, max_overflow=scfg.MAX_OVERFLOW)
Base = declarative_base()

def new_Scoped_session():
   return scoped_session(sessionmaker(bind=Engine, autoflush=scfg.AUTO_FLUSH, autocommit=scfg.AUTO_COMMIT))

def new_Session():
   return sessionmaker(bind=Engine, autoflush=scfg.AUTO_FLUSH, autocommit=scfg.AUTO_COMMIT).begin()
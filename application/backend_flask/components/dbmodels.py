from sqlalchemy import Column, ForeignKey, event
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import mysql as ms
from .dbsettings import Base, Engine
from datetime import datetime, timezone
import os
from .config import STORAGE_PATH


# RELATIONSHIP: https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
# SCHEMA ATTRIBUTES: https://docs.sqlalchemy.org/en/14/core/metadata.html


# ==============================================================================
class AccountInfo (Base):
    __tablename__ = 'ACCOUNTINFO'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(128), nullable=False)
    Birthdate = Column(ms.DATETIME)
    Gender = Column(ms.TINYINT) # 1: male, 2: female
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_ImageProfile = Column(ms.INTEGER, ForeignKey('IMAGEPROFILE.ID'))
    rel_ImageProfile = relationship('ImageProfile', cascade='save-update, merge, delete')
    
    ## Account reference
    rel_Account = relationship("Account", back_populates="rel_AccountInfo", uselist=False)
      
    
# ==============================================================================
class Account (Base):
    __tablename__ = 'ACCOUNT'
    ID = Column(ms.INTEGER, primary_key=True)
    Username = Column(ms.NVARCHAR(128), nullable=False)
    Password = Column(ms.NVARCHAR(256), nullable=False)
    Email = Column(ms.NVARCHAR(128), nullable=False)
    Account_type = Column(ms.TINYINT, nullable=False) # 0: user, 1: admin, 2: test
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_AccountInfo = Column(ms.INTEGER, ForeignKey("ACCOUNTINFO.ID"), nullable=False)
    rel_AccountInfo = relationship("AccountInfo", cascade='save-update, merge, delete', back_populates="rel_Account")
    
    ## Rating reference
    rel_Rating = relationship("Rating", back_populates="rel_Account")
    
    ## Like reference
    rel_Like = relationship("Like", back_populates="rel_Account")
    
    ## View reference
    rel_View = relationship("View", back_populates="rel_Account")

    
# ==============================================================================
class ImageProfile (Base):
    __tablename__ = 'IMAGEPROFILE'
    ID = Column(ms.INTEGER, primary_key=True)
    Filename = Column(ms.NVARCHAR(64), nullable=False)


@event.listens_for(ImageProfile, 'after_delete')
def receive_after_delete(mapper, connection, target):
    os.remove(os.path.join(STORAGE_PATH, 'profile/', target.Filename))


# ==============================================================================
class ImageAnime (Base):
    __tablename__ = 'IMAGEANIME'
    ID = Column(ms.INTEGER, primary_key=True)
    Filename = Column(ms.NVARCHAR(64), nullable=False)
    
    ID_Anime = Column(ms.INTEGER, ForeignKey("ANIME.ID"))
    rel_Anime = relationship("Anime", back_populates="rel_ImageAnime")


@event.listens_for(ImageAnime, 'after_delete')
def receive_after_delete(mapper, connection, target):
    if os.path.exists(os.path.join(STORAGE_PATH, 'anime/', target.Filename)):
        os.remove(os.path.join(STORAGE_PATH, 'anime/', target.Filename))


# ==============================================================================
class Rating (Base):
    __tablename__ = 'RATING'
    ID = Column(ms.INTEGER, primary_key=True)
    Point = Column(ms.FLOAT, nullable=False)
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Account = Column(ms.INTEGER, ForeignKey("ACCOUNT.ID"), nullable=False)
    rel_Account = relationship("Account", back_populates="rel_Rating")
    
    
# ==============================================================================
class Like (Base):
    __tablename__ = 'LIKE'
    ID = Column(ms.INTEGER, primary_key=True)
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Account = Column(ms.INTEGER, ForeignKey("ACCOUNT.ID"), nullable=False)
    rel_Account = relationship("Account", back_populates="rel_Like")
        
    
# ==============================================================================
class View (Base):
    __tablename__ = 'VIEW'
    ID = Column(ms.INTEGER, primary_key=True)
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Account = Column(ms.INTEGER, ForeignKey("ACCOUNT.ID"), nullable=False)
    rel_Account = relationship("Account", back_populates="rel_View")
        
    
# ==============================================================================
class AnimeRating (Base):
    __tablename__ = 'ANIMERATING'
    ID = Column(ms.INTEGER, primary_key=True)
    Rating = Column(ms.NVARCHAR(32), nullable=False)
    
    rel_Anime = relationship("Anime", back_populates="rel_AnimeRating")

    
# ==============================================================================
class Anime (Base):
    __tablename__ = 'ANIME'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(128), nullable=False)
    Genres = Column(ms.NVARCHAR(128))
    Score = Column(ms.FLOAT)
    Episodes = Column(ms.NVARCHAR(10))
    
    ID_AnimeInfo = Column(ms.INTEGER, ForeignKey("ANIMEINFO.ID"), nullable=False)
    rel_AnimeInfo = relationship("AnimeInfo", cascade='save-update, merge, delete', back_populates="rel_Anime")
    
    ID_AnimeRating = Column(ms.INTEGER, ForeignKey("ANIMERATING.ID"), nullable=False)
    rel_AnimeRating = relationship("AnimeRating", back_populates="rel_Anime")
    
    # ImageAnime references
    rel_ImageAnime = relationship("ImageAnime", cascade='save-update, merge, delete', back_populates="rel_Anime")
    
    
# ==============================================================================
class AnimeInfo (Base):
    __tablename__ = 'ANIMEINFO'
    ID = Column(ms.INTEGER, primary_key=True)
    Name_ENG = Column(ms.NVARCHAR(128))
    Name_JPN = Column(ms.NVARCHAR(128))
    Synopsis = Column(ms.NVARCHAR(4000))
    Type = Column(ms.NVARCHAR(16))
    Popularity = Column(ms.SMALLINT)
    Aired = Column(ms.NVARCHAR(128))
    Premiered = Column(ms.NVARCHAR(32))
    Producers = Column(ms.NVARCHAR(512))
    Licensors = Column(ms.NVARCHAR(256))
    Studio = Column(ms.NVARCHAR(256))
    Source = Column(ms.NVARCHAR(32))
    Duration = Column(ms.NVARCHAR(64))
    
    rel_Anime = relationship("Anime", back_populates="rel_AnimeInfo", uselist=False)
    
    
# ==============================================================================
#Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)
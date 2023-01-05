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
class Permission (Base):
    __tablename__ = 'PERMISSION'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(50), nullable=False)
    
    ## Account reference
    rel_Account = relationship("Account", back_populates="rel_Permission")


# ==============================================================================
class AccountInfo (Base):
    __tablename__ = 'ACCOUNTINFO'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(128), nullable=False)
    Birthdate = Column(ms.DATETIME)
    Gender = Column(ms.TINYINT) # 1: male, 2: female
    Phone_number = Column(ms.VARCHAR(12))
    Identification_number = Column(ms.VARCHAR(12))
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Image_Profile = Column(ms.INTEGER, ForeignKey('IMAGE.ID'))
    rel_Image_Profile = relationship('Image', foreign_keys=[ID_Image_Profile], cascade='save-update, merge, delete', back_populates='rel_AccountInfo_Profile')
    
    ID_Image_Identity = Column(ms.INTEGER, ForeignKey('IMAGE.ID'))
    rel_Image_Identity = relationship('Image', foreign_keys=[ID_Image_Identity], cascade='save-update, merge, delete', back_populates='rel_AccountInfo_Identity')
    
    ## Account reference
    rel_Account = relationship("Account", back_populates="rel_AccountInfo", uselist=False)
    
    ## Address reference
    rel_Address = relationship('Address', back_populates='rel_AccountInfo')
    
    
# ==============================================================================
class AccountStat (Base):
    __tablename__ = 'ACCOUNTSTAT'
    ID = Column(ms.INTEGER, primary_key=True)
    General_rating = Column(ms.FLOAT, nullable=False, default=-1)
    Reply_percentage = Column(ms.FLOAT, nullable=False, default=-1)
    Avg_reply_time = Column(ms.FLOAT, nullable=False, default=-1)
    
    ## Account reference
    rel_Account = relationship('Account', back_populates='rel_AccountStat', uselist=False)
    
    
# ==============================================================================
class Account (Base):
    __tablename__ = 'ACCOUNT'
    ID = Column(ms.INTEGER, primary_key=True)
    Username = Column(ms.NVARCHAR(128), nullable=False)
    Password = Column(ms.NVARCHAR(256), nullable=False)
    Email = Column(ms.NVARCHAR(128), nullable=False)
    Account_type = Column(ms.TINYINT, nullable=False) # 0: default account, 1: google account, 2: facebook account, 3: placeholder account
    
    ID_AccountStat = Column(ms.INTEGER, ForeignKey('ACCOUNTSTAT.ID'), nullable=False)
    rel_AccountStat = relationship('AccountStat', cascade='save-update, merge, delete', back_populates='rel_Account')
    
    ID_Permission = Column(ms.INTEGER, ForeignKey("PERMISSION.ID"), nullable=False)
    rel_Permission = relationship("Permission", back_populates="rel_Account")
    
    ID_AccountInfo = Column(ms.INTEGER, ForeignKey("ACCOUNTINFO.ID"), nullable=False)
    rel_AccountInfo = relationship("AccountInfo", cascade='save-update, merge, delete', back_populates="rel_Account")

    ## Post reference
    rel_Post = relationship("Post", back_populates="rel_Account")
    
    ## Rating reference
    rel_Rating = relationship("Rating", back_populates="rel_Account")
    
    ## Like reference
    rel_Like = relationship("Like", back_populates="rel_Account")
    
    ## View reference
    rel_View = relationship("View", back_populates="rel_Account")
    
    ## ChatParticipant reference
    rel_ChatParticipant = relationship("ChatParticipant", back_populates="rel_Account")


# ==============================================================================
class Ward (Base):
    __tablename__ = 'WARD'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(50), nullable=False)

    ID_District = Column(ms.INTEGER, ForeignKey("DISTRICT.ID"), nullable=False)
    rel_District = relationship("District", back_populates="rel_Ward")


# ==============================================================================
class District (Base):
    __tablename__ = 'DISTRICT'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(50), nullable=False)

    ID_City = Column(ms.INTEGER, ForeignKey("CITY.ID"), nullable=False)
    rel_City = relationship("City", back_populates="rel_District")
    
    ## Ward reference
    rel_Ward = relationship('Ward', back_populates='rel_District')
    
    
# ==============================================================================
class City (Base):
    __tablename__ = 'CITY'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(50), nullable=False)
    
    ## District reference
    rel_District = relationship("District", back_populates="rel_City")
    
    
# ==============================================================================
class Address (Base):
    __tablename__ = 'ADDRESS'
    ID = Column(ms.INTEGER, primary_key=True)
    Detail_address = Column(ms.NVARCHAR(128))
    
    ID_AccountInfo = Column(ms.INTEGER, ForeignKey("ACCOUNTINFO.ID"), nullable=False)
    rel_AccountInfo = relationship("AccountInfo", back_populates="rel_Address")
    
    ID_City = Column(ms.INTEGER, ForeignKey("CITY.ID"), nullable=False)
    rel_City = relationship("City")
        
    ID_District = Column(ms.INTEGER, ForeignKey("DISTRICT.ID"), nullable=False)
    rel_District = relationship("District")
    
    ID_Ward = Column(ms.INTEGER, ForeignKey("WARD.ID"), nullable=False)
    rel_Ward = relationship("Ward")

    ## Post reference
    rel_Post = relationship("Post", back_populates="rel_Address")
        
    
# ==============================================================================
class Post (Base):
    __tablename__ = 'POST'
    ID = Column(ms.INTEGER, primary_key=True)
    Title = Column(ms.NVARCHAR(128), nullable=False)
    Content = Column(ms.NVARCHAR(2000))
    Pricetag = Column(ms.BIGINT)
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Account = Column(ms.INTEGER, ForeignKey("ACCOUNT.ID"), nullable=False)
    rel_Account = relationship("Account", back_populates="rel_Post")
    
    ID_Address = Column(ms.INTEGER, ForeignKey("ADDRESS.ID"), nullable=False)
    rel_Address = relationship("Address", back_populates="rel_Post")
    
    ID_VehicleInfo = Column(ms.INTEGER, ForeignKey("VEHICLEINFO.ID"), nullable=False)
    rel_VehicleInfo = relationship("VehicleInfo", back_populates="rel_Post")
    
    ID_PostStat = Column(ms.INTEGER, ForeignKey('POSTSTAT.ID'), nullable=False)
    rel_PostStat = relationship('PostStat', back_populates='rel_Post')

    ## ImagePost reference
    rel_Image = relationship("Image", back_populates="rel_Post")
    
    ## PostStatus reference
    rel_PostStatus = relationship("PostStatus", back_populates="rel_Post")
    
    ## Rating reference
    rel_Rating = relationship("Rating", back_populates="rel_Post")
    
    ## Like reference
    rel_Like = relationship("Like", back_populates="rel_Post")
    
    ## View reference
    rel_View = relationship("View", back_populates="rel_Post")
    
    ## ChatRoom reference
    rel_ChatRoom = relationship("ChatRoom", back_populates="rel_Post", uselist=False)
    

# ==============================================================================
class Image (Base):
    __tablename__ = 'IMAGE'
    ID = Column(ms.INTEGER, primary_key=True)
    Filename = Column(ms.NVARCHAR(64), nullable=False)
    
    ID_Post = Column(ms.INTEGER, ForeignKey("POST.ID"))
    rel_Post = relationship("Post", back_populates="rel_Image")
    
    ID_ImageType = Column(ms.INTEGER, ForeignKey('IMAGETYPE.ID'))
    rel_ImageType = relationship('ImageType')
    
    ## AccountInfo reference
    rel_AccountInfo_Profile = relationship('AccountInfo', foreign_keys=[AccountInfo.ID_Image_Profile], back_populates='rel_Image_Profile')
    
    ## AccountInfo reference
    rel_AccountInfo_Identity = relationship('AccountInfo', foreign_keys=[AccountInfo.ID_Image_Identity], back_populates='rel_Image_Identity')
    

@event.listens_for(Image, 'after_delete')
def receive_after_delete(mapper, connection, target):
    if target.ID_ImageType == 1: folder = 'post/'
    elif target.ID_ImageType == 2: folder = 'logo/'
    elif target.ID_ImageType == 3: folder = 'user/'
    elif target.ID_ImageType == 4: folder = 'identity/'
    os.remove(os.path.join(STORAGE_PATH, folder, target.Filename))


# ==============================================================================
class ImageType (Base):
    __tablename__ = 'IMAGETYPE'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(32), nullable=False)


# ==============================================================================
class PostStatus (Base):
    __tablename__ = 'POSTSTATUS'
    ID = Column(ms.INTEGER, primary_key=True)
    Status = Column(ms.NVARCHAR(50), nullable=False)
    Time_updated = Column(ms.DATETIME, default=datetime.now(timezone.utc))

    ID_Post = Column(ms.INTEGER, ForeignKey("POST.ID"), nullable=False)
    rel_Post = relationship("Post", back_populates="rel_PostStatus", uselist=False)
    
    
# ==============================================================================
class PostStat (Base):
    __tablename__ = 'POSTSTAT'
    ID = Column(ms.INTEGER, primary_key=True)
    View_amount = Column(ms.INTEGER, nullable=False)
    Like_amount = Column(ms.INTEGER, nullable=False)
    Contact_amount = Column(ms.INTEGER, nullable=False)
    
    ## Post reference
    rel_Post = relationship("Post", back_populates="rel_PostStat", uselist=False)
    
    
# ==============================================================================
class Rating (Base):
    __tablename__ = 'RATING'
    ID = Column(ms.INTEGER, primary_key=True)
    Rating_point = Column(ms.FLOAT, nullable=False)
    Content = Column(ms.NVARCHAR(2000))
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Post = Column(ms.INTEGER, ForeignKey("POST.ID"), nullable=False)
    rel_Post = relationship("Post", back_populates="rel_Rating")
    
    ID_Account = Column(ms.INTEGER, ForeignKey("ACCOUNT.ID"), nullable=False)
    rel_Account = relationship("Account", back_populates="rel_Rating")
    
    
    
# ==============================================================================
class Like (Base):
    __tablename__ = 'LIKE'
    ID = Column(ms.INTEGER, primary_key=True)
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Post = Column(ms.INTEGER, ForeignKey("POST.ID"), nullable=False)
    rel_Post = relationship("Post", back_populates="rel_Like")
    
    ID_Account = Column(ms.INTEGER, ForeignKey("ACCOUNT.ID"), nullable=False)
    rel_Account = relationship("Account", back_populates="rel_Like")
        
    
# ==============================================================================
class View (Base):
    __tablename__ = 'VIEW'
    ID = Column(ms.INTEGER, primary_key=True)
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Post = Column(ms.INTEGER, ForeignKey("POST.ID"), nullable=False)
    rel_Post = relationship("Post", back_populates="rel_View")
    
    ID_Account = Column(ms.INTEGER, ForeignKey("ACCOUNT.ID"), nullable=False)
    rel_Account = relationship("Account", back_populates="rel_View")
        
    
# ==============================================================================
class VehicleInfo (Base):
    __tablename__ = 'VEHICLEINFO'
    ID = Column(ms.INTEGER, primary_key=True)
    Vehicle_name = Column(ms.NVARCHAR(128))
    Odometer = Column(ms.INTEGER)
    License_plate = Column(ms.NVARCHAR(10))
    Manufacture_year = Column(ms.MEDIUMINT)
    Cubic_power = Column(ms.INTEGER)

    ID_VehicleBrand = Column(ms.INTEGER, ForeignKey("VEHICLEBRAND.ID"), nullable=False)
    rel_VehicleBrand = relationship("VehicleBrand")
    
    ID_VehicleLineup = Column(ms.INTEGER, ForeignKey("VEHICLELINEUP.ID"))
    rel_VehicleLineup = relationship("VehicleLineup")
    
    ID_VehicleType = Column(ms.INTEGER, ForeignKey("VEHICLETYPE.ID"), nullable=False)
    rel_VehicleType = relationship("VehicleType")
    
    ID_Condition = Column(ms.INTEGER, ForeignKey("VEHICLECONDITION.ID"), nullable=False)
    rel_Condition = relationship("VehicleCondition")
    
    ID_Color = Column(ms.INTEGER, ForeignKey("COLOR.ID"))
    rel_Color = relationship("Color")

    ## Post reference
    rel_Post = relationship("Post", back_populates="rel_VehicleInfo", uselist=False)
    
    
# ==============================================================================
class VehicleBrand (Base):
    __tablename__ = 'VEHICLEBRAND'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(50), nullable=False)
    
    ID_Image = Column(ms.INTEGER, ForeignKey("IMAGE.ID"), nullable=True)
    rel_Image = relationship("Image")
    
    
# ==============================================================================
class VehicleLineup (Base):
    __tablename__ = 'VEHICLELINEUP'
    ID = Column(ms.INTEGER, primary_key=True)
    Lineup = Column(ms.NVARCHAR(50), nullable=False)

    ID_VehicleBrand = Column(ms.INTEGER, ForeignKey("VEHICLEBRAND.ID"), nullable=False)
    rel_VehicleBrand = relationship('VehicleBrand')
    
# ==============================================================================
class VehicleType (Base):
    __tablename__ = 'VEHICLETYPE'
    ID = Column(ms.INTEGER, primary_key=True)
    Type = Column(ms.NVARCHAR(50), nullable=False)
    
    
# ==============================================================================
class VehicleCondition (Base):
    __tablename__ = 'VEHICLECONDITION'
    ID = Column(ms.INTEGER, primary_key=True)
    Condition = Column(ms.NVARCHAR(50), nullable=False)
    
    
# ==============================================================================
class Color (Base):
    __tablename__ = 'COLOR'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(20), nullable=False)
    Color_hex = Column(ms.NVARCHAR(6), nullable=False)
    
    
# ==============================================================================
class ChatRoom (Base):
    __tablename__ = 'CHATROOM'
    ID = Column(ms.INTEGER, primary_key=True)
    Time_created = Column(ms.DATETIME, nullable=False, default=datetime.now(timezone.utc))
    
    ID_Post = Column(ms.INTEGER, ForeignKey("POST.ID"))
    rel_Post = relationship("Post", back_populates="rel_ChatRoom")

    ## ChatRoom reference
    rel_ChatParticipant = relationship("ChatParticipant", back_populates="rel_ChatRoom")
    
    ## ChatMessage reference
    rel_ChatMessage = relationship("ChatMessage", back_populates="rel_ChatRoom")
    
    
# ==============================================================================
class ChatParticipant (Base):
    __tablename__ = 'CHATPARTICIPANT'
    ID = Column(ms.INTEGER, primary_key=True)
    
    ID_ChatRoom = Column(ms.INTEGER, ForeignKey("CHATROOM.ID"), nullable=False)
    rel_ChatRoom = relationship("ChatRoom", back_populates="rel_ChatParticipant")
    
    ID_Account = Column(ms.INTEGER, ForeignKey("ACCOUNT.ID"), nullable=False)
    rel_Account = relationship("Account", back_populates="rel_ChatParticipant")
    
    ## ChatMessage reference
    rel_ChatMessage = relationship("ChatMessage", back_populates="rel_ChatParticipant")
    
    
# ==============================================================================
class ChatMessage (Base):
    __tablename__ = 'CHATMESSAGE'
    ID = Column(ms.INTEGER, primary_key=True)
    Content = Column(ms.NVARCHAR(2000), nullable=False)
    Time_created = Column(ms.DATETIME, default=datetime.now(timezone.utc))
    
    ID_ChatRoom = Column(ms.INTEGER, ForeignKey("CHATROOM.ID"), nullable=False)
    rel_ChatRoom = relationship("ChatRoom", back_populates="rel_ChatMessage")
    
    ID_ChatParticipant = Column(ms.INTEGER, ForeignKey("CHATPARTICIPANT.ID"), nullable=False)
    rel_ChatParticipant = relationship("ChatParticipant", back_populates="rel_ChatMessage")
    

# ==============================================================================
class Version (Base):
    __tablename__ = 'VERSION'
    ID = Column(ms.INTEGER, primary_key=True)
    Name = Column(ms.NVARCHAR(16), nullable=False)
    Version = Column(ms.NVARCHAR(16), nullable=False)
    
    
# ==============================================================================
# Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)
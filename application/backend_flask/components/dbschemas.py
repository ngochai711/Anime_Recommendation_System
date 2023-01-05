from marshmallow_sqlalchemy import SQLAlchemySchema as Schema, auto_field
from components import dbmodels as dbm

class AccountSchema(Schema):
    class Meta:
        model = dbm.Account
        load_instance = True
        # include_relationships = True
        # include_fk = False   # default value: False
        
    ID = auto_field()
    Username = auto_field()
    ID_Permission = auto_field()
    ID_AccountInfo = auto_field()
    ID_AccountStat = auto_field()
        
        
class PermissionSchema(Schema):
    class Meta:
        model = dbm.Permission
        load_instance = True

    ID = auto_field()
    Name = auto_field()
    

class AccountInfoSchema(Schema):
    class Meta:
        model = dbm.AccountInfo
        load_instance = True
        
    ID = auto_field()
    Name = auto_field()
    Birthdate = auto_field()
    Gender = auto_field()
    Phone_number = auto_field()
    Identification_number = auto_field()
    
    
class AddressSchema(Schema):
    class Meta:
        model = dbm.Address
        load_instance = True
        
    ID = auto_field()
    Detail_address = auto_field()
    ID_City = auto_field()
    ID_District = auto_field()
    ID_Ward = auto_field()

class WardSchema(Schema):
    class Meta:
        model = dbm.Ward
        load_instance = True
        
    ID = auto_field()
    Name = auto_field()
    ID_District = auto_field()

class DistrictSchema(Schema):
    class Meta:
        model = dbm.District
        load_instance = True
        
    ID = auto_field()
    Name = auto_field()
    ID_City = auto_field()


class CitySchema(Schema):
    class Meta:
        model = dbm.City
        load_instance = True
        
    ID = auto_field()
    Name = auto_field()

class ImageTypeSchema(Schema):
    class Meta:
        model = dbm.ImageType
        load_instance = True
        
    ID = auto_field()
    Name = auto_field()

class VersionSchema(Schema):
    class Meta:
        model = dbm.Version
        load_instance = True
        
    ID = auto_field()
    Name = auto_field()
    Version = auto_field()



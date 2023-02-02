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
    Account_type = auto_field()
    ID_AccountInfo = auto_field()
    
    
class AccountInfoSchema(Schema):
    class Meta:
        model = dbm.AccountInfo
        load_instance = True
    
    ID = auto_field()
    Name = auto_field()
    Birthdate = auto_field()
    Gender = auto_field()
    
    
class AnimeSchema(Schema):
    class Meta:
        model = dbm.Anime
        load_instance = True
        
    ID = auto_field()
    Name = auto_field()
    Genres = auto_field()
    Score = auto_field()
    Episodes = auto_field()
    rel_AnimeImage = auto_field()
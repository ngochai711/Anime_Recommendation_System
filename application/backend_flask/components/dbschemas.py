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
    Time_created = auto_field()
    rel_ImageAnime = auto_field()
    ID_AnimeRating = auto_field()
    

class AnimeRatingSchema(Schema):
    class Meta:
        model = dbm.AnimeRating
        load_instance = True
        
    ID = auto_field()
    Rating = auto_field()
    
    
class AnimeInfoSchema(Schema):
    class Meta:
        model = dbm.AnimeInfo
        load_instance = True
    
    ID = auto_field()
    Name_ENG = auto_field()
    Name_JPN = auto_field()
    Synopsis = auto_field()
    Type = auto_field()
    Popularity = auto_field()
    Aired = auto_field()
    Premiered = auto_field()
    Producers = auto_field()
    Licensors = auto_field()
    Studio = auto_field()
    Source = auto_field()
    Duration = auto_field()
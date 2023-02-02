from flask import jsonify
from .dbmodels import *
from .dbschemas import *
from .dbsettings import new_Scoped_session
import pandas as pd
import numpy as np
from .config import STORAGE_PATH, HOME_DIRECTORY
import requests
from components.imagescraping import get_original_images_custom
from urllib.parse import urlparse


# def InsertLocation2():
#     TruncateTables({"CITY", "DISTRICT", "WARD"})
#     city_table = pd.read_csv(INITIALDATA + 'Locations_City.csv', index_col=False)
#     district_table = pd.read_csv(INITIALDATA + 'Locations_District.csv', index_col=False)
#     ward_table = pd.read_csv(INITIALDATA + 'Locations_Ward.csv', index_col=False)
#     Session = new_Scoped_session()
#     try:
#         for table in [city_table, district_table, ward_table]:
#             for i, row in table.iterrows():
#                 if table is city_table: new_row = City(ID=row['City_UID'], Name=row['City'])
#                 elif table is district_table: new_row = District(ID=row['District_UID'], Name=row['District'], ID_City=row['City_UID'])
#                 else: new_row = Ward(ID=row['Ward_UID'], Name=row['Ward'], ID_District=row['District_UID'])
#                 Session.add(new_row)
#             Session.flush()
#         Session.commit()
#         return "Inserted {} cities, {} districts, {} wards".format(city_table.shape[0], district_table.shape[0], ward_table.shape[0])
#     except Exception as e:
#         Session.rollback()
#         return "Error: " + str(e)


def TruncateTables(tables: list):
    Session = new_Scoped_session()
    Session.execute("SET FOREIGN_KEY_CHECKS=0;")
    Session.commit()
    for table in tables:
        try:
            Session.execute("TRUNCATE TABLE {};".format(table))
        except Exception as e:
            if "1146" in str(e):
                print("Table {} does not exist".format(table))
            else:
                print("Truncate table {} error: {}".format(table,e))

    Session.execute("SET FOREIGN_KEY_CHECKS=1;")
    Session.commit()
    Session.close()


def GetImageFolder(image_type):
    if image_type == 1: folder = 'anime/'
    elif image_type == 2: folder = 'profile/'
    return folder


def SaveImageFromURL(Session, url, image_type, anime_id):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    r = requests.get(url, headers=headers)
    if r.status_code==200:
        urlname = urlparse(url)
        filename = os.path.basename(urlname.path)
        ext = filename.split('.')[-1]
        if image_type == 1: image = ImageAnime(Filename="temp", ID_Anime=anime_id)
        elif image_type == 2: image = ImageProfile(Filename="temp")
        Session.add(image)
        Session.flush()
        image.Filename = str(image.ID) + '.' + ext
        open(STORAGE_PATH + GetImageFolder(image_type) + image.Filename, "wb").write(r.content)
        Session.flush()
        return [True, image.ID]
    return [False, "Invalid response"]


def SaveProfileImage(Session, file):
    if file.filename == "":
        return [False, "No file selected"]
    ext = file.filename.split('.')[-1]
    if ext not in ['jpg', 'jpeg', 'png']:
        return [False, "File extension not supported"]
    try:
        new_image = ImageProfile(Filename="temp")
        Session.add(new_image)
        Session.flush()
        new_image.Filename = str(new_image.ID) + '.' + ext
        Session.commit()
        file.save(os.path.join(STORAGE_PATH, 'profile/', str(new_image.ID) + '.' + ext))
        return [True, new_image]
    except Exception as e:
        Session.rollback()
        return [False, str(e)]


def SetupAccount(Session, a_email, a_username, a_password, a_account_type, i_name, i_image=None):
   try:
      account = dbm.Account(Username=a_username, Password=a_password, Email=a_email, Account_type=a_account_type)
      accountinfo = dbm.AccountInfo(Name=i_name)
      if i_image != None: 
         output = SaveImageFromURL(Session, i_image, 3)
         if output[0]: accountinfo.ID_ImageProfile = output[1]
      Session.add(accountinfo)
      Session.flush()
      account.ID_AccountInfo = accountinfo.ID
      Session.add(account)
      Session.flush()
      return [True, account]
   except Exception as e:
      return [False, str(e)]
    
    
def InsertTestAccounts(amount):
    Session = new_Scoped_session()
    try:
        oldtestusers = Session.query(Account).filter(Account.Account_type==2).all()
        for i in oldtestusers:
            Session.remove(i)
        Session.flush()
        acc_list = []
        accinfo_list = []
        for i in range(amount):
            output = SetupAccount(Session, f"testuser{i}@email.com", f"testuser{i}", "testuserpassword", 3, 4, f"Anime Testuser {i}", "0123456789", None)
            if output[0] == False:
                Session.rollback()
                return jsonify({"msg": "Incompleted", "err": f"testuser{i} failed - {str(output[1])}"})
            else:
                acc_list.append(output[1].ID)
                accinfo_list.append(output[1].ID_AccountInfo)
                print(f"testuser{i}: Succeed")
        Session.commit()
        return jsonify({"msg": "Completed", "err": "", "acc_list": acc_list, "accinfo_list": accinfo_list})
    except Exception as e:
        Session.rollback()
        return jsonify({"msg": "Incompleted", "err": str(e)})


def InsertAnimes(Session):
    TruncateTables({"ANIME", "ANIMERATING", "ANIMEINFO"})
    anime_table = pd.read_csv(HOME_DIRECTORY + "../../dataset/db_anime.csv")
    rating_table = pd.read_csv(HOME_DIRECTORY + "../../dataset/db_rating.csv")
    anime_table = anime_table.replace({np.nan: None})
    try:
        for i, row in rating_table.iterrows():
            new_rating = AnimeRating(Rating=row['Rating'])
            Session.add(new_rating)
        Session.flush()
        
        for i, row in anime_table.iterrows():
            new_animeinfo = AnimeInfo(
                ID = row['MAL_ID'],
                Name_ENG = row['English name'],
                Name_JPN = row['Japanese name'],
                Synopsis = row['sypnopsis'],
                Type = row['Type'],
                Popularity = row['Popularity'],
                Aired = row['Aired'],
                Premiered = row['Premiered'],
                Producers = row['Producers'],
                Licensors = row['Licensors'],
                Studio = row['Studios'],
                Source = row['Source'],
                Duration = row['Duration']
            )
            Session.add(new_animeinfo)
            Session.flush()
            new_anime = Anime(
                ID = row['MAL_ID'],
                Name = row['Name'],
                Genres = row['Genres'],
                Score = row['Score'],
                Episodes = row['Episodes'],
                ID_AnimeInfo = row['MAL_ID'],
                ID_AnimeRating = row['Rating']
            )
            Session.add(new_anime)
            Session.flush()
        return [True]
    except Exception as e:
        Session.rollback()
        return [False, str(e)]
    

def InsertAnimeImages(Session):
    Session = new_Scoped_session()
    try:
        # old = Session.query(ImageAnime).all()
        # Session.remove(old)
        # Session.flush()
        anime_table = pd.read_csv(HOME_DIRECTORY + "../../dataset/db_anime.csv")
        for index, row in anime_table.iterrows():
            if index % 5 == 0: print(f"Currently at anime id {row['MAL_ID']}")
            image_list = get_original_images_custom(row['Name'])
            for key, value in image_list.items():
                if key <= 3: 
                    output = SaveImageFromURL(Session, str(value), 1, row['MAL_ID'])
                    if output[0] == False:
                        print(f"Anime id {row['MAL_ID']} with link '{value}' got invalid response, skipping")
                else: break
        Session.commit()
        return [True]
    except Exception as e:
        return [False, str(e)]
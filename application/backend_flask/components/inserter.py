from flask import jsonify
import openpyxl, unicodedata
from .dbmodels import *
from .dbschemas import *
from .dbsettings import new_Scoped_session
import pandas as pd
from .config import STORAGE_PATH
import requests


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
    

def SaveImageFromURL(Session, url, image_type, anime_id):
    r = requests.get(url)
    if r.status_code==200:
        filename = url.split('/')[-1]
        open(os.path.join(STORAGE_PATH, image_type, filename), "wb").write(r.content)
        if image_type == 'profile':
            image = ImageProfile(Filename=filename)
        elif image_type == 'anime':
            image = ImageAnime(Filename=filename, ID_Anime=anime_id)
        Session.add(image)
        Session.flush()
        ext = image.Filename.split('.')[-1]
        image.Filename = str(image.ID) + '.' + ext
        Session.flush()
        return [True, image.ID]
    return [False]


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

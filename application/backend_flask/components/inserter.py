from flask import jsonify
import openpyxl, unicodedata
from .dbmodels import *
from .dbschemas import *
from .dbsettings import new_Scoped_session
import pandas as pd
from .config import STORAGE_PATH
import requests
INITIALDATA = "components/initial_data/"

def InitialDataFile(name: str):
    return INITIALDATA + name + ".xlsx"

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


def remove_accents(input_str = None):
    print(f"Debug: {input_str}")
    if input_str == None:
        return ''
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nkfd_form.encode('ASCII', 'ignore')
    return only_ascii.decode()

def InsertLocation1():
    
    TruncateTables({"CITY", "DISTRICT", "WARD"})
    wb = openpyxl.load_workbook(InitialDataFile("Locations"))

    sheet = wb.active
    i = 1
    c = 0
    d = 0
    w = 0
    Session = new_Scoped_session()
    cities = []
    districts = []
    wards = []
    
    while True:
        i += 1
        cityName = sheet.cell(row=i, column=1).value
        if cityName == None:
            break
        districtName = sheet.cell(row=i, column=3).value
        wardName = sheet.cell(row=i, column=5).value

        if cityName not in cities:
            city = City(Name=cityName)
            Session.add(city)
            cities.append(cityName)
            c += 1
        
        cityID = c

        tempDistrict = {
            "Name": districtName,
            "CityID": cityID
        }

        if tempDistrict not in districts:
            district = District(Name=districtName, ID_City=cityID)
            Session.add(district)
            districts.append(tempDistrict)
            d += 1

        districtID = d

        if wardName == None:
            continue

        tempWard = {
            "Name": wardName,
            "DistrictID": districtID
        }

        if tempWard not in wards:
            ward = Ward(Name=wardName, ID_District=districtID)
            Session.add(ward)
            wards.append(tempWard)
            w += 1

    Session.commit()
    Session.close()
    return "Inserted {} cities, {} districts, {} wards".format(c, d, w)


def InsertLocation2():
    TruncateTables({"CITY", "DISTRICT", "WARD"})
    city_table = pd.read_csv(INITIALDATA + 'Locations_City.csv', index_col=False)
    district_table = pd.read_csv(INITIALDATA + 'Locations_District.csv', index_col=False)
    ward_table = pd.read_csv(INITIALDATA + 'Locations_Ward.csv', index_col=False)
    Session = new_Scoped_session()
    try:
        for table in [city_table, district_table, ward_table]:
            for i, row in table.iterrows():
                if table is city_table: new_row = City(ID=row['City_UID'], Name=row['City'])
                elif table is district_table: new_row = District(ID=row['District_UID'], Name=row['District'], ID_City=row['City_UID'])
                else: new_row = Ward(ID=row['Ward_UID'], Name=row['Ward'], ID_District=row['District_UID'])
                Session.add(new_row)
            Session.flush()
        Session.commit()
        return "Inserted {} cities, {} districts, {} wards".format(city_table.shape[0], district_table.shape[0], ward_table.shape[0])
    except Exception as e:
        Session.rollback()
        return "Error: " + str(e)
    
    
def InsertPermission():
    TruncateTables({"Permission"})
    wb = openpyxl.load_workbook(InitialDataFile("Permissions"))

    sheet = wb.active
    i = 1
    p = 0

    Session = new_Scoped_session()
    while True:
        i += 1
        name = sheet.cell(row=i, column=1).value
        if name == None:
            break
        perm = Session.query(Permission).filter(Permission.Name == name).first()
        if perm == None or perm.Name != name:
            perm = Permission(Name=name)
            Session.add(perm)
            p += 1

    Session.commit()
    Session.close()

    return "Inserted {} permissions".format(p)

def InsertImageType():
    TruncateTables({"ImageType"})
    wb = openpyxl.load_workbook(InitialDataFile("ImageTypes"))
    Session = new_Scoped_session()
    sheet = wb.active
    i = 1
    it = 0
    while True:
        i += 1
        name = sheet.cell(row=i, column=1).value
        if name == None:
            break
        imgType = Session.query(ImageType).filter(ImageType.Name == name).first()
        if imgType == None or imgType.Name != name:
            imgType = ImageType(Name=name)
            Session.add(imgType)
            it += 1

    Session.commit()
    Session.close()

    return "Inserted {} image types".format(it)


def SaveImageFromURL(Session, url, image_type):
    r = requests.get(url)
    if r.status_code==200:
        filename = url.split('/')[-1]
        if image_type == 1: folder = 'post/'
        elif image_type == 2: folder = 'logo/'
        elif image_type == 3: folder = 'user/'
        elif image_type == 4: folder = 'identity/'
        open(STORAGE_PATH + folder + filename, "wb").write(r.content)
        image = Image(Filename=filename, ID_ImageType=image_type)
        Session.add(image)
        Session.flush()
        ext = image.Filename.split('.')[-1]
        image.Filename = str(image.ID) + '.' + ext
        Session.flush()
        return [True, image.ID]
    return [False]


def SetupAccount(Session, a_email, a_username, a_password, a_type, a_permission, i_name, i_phone=None, i_image=None):
   try:
      account = dbm.Account(Username=a_username, Password=a_password, Email=a_email, Account_type=a_type, ID_Permission=a_permission)
      accountinfo = dbm.AccountInfo(Name=i_name, Phone_number=i_phone)
      accountstat = dbm.AccountStat()
      if i_image != None: 
         output = SaveImageFromURL(Session, i_image, 3)
         if output[0]: accountinfo.ID_Image_Profile = output[1]
      Session.add(accountstat)
      Session.add(accountinfo)
      Session.flush()
      account.ID_AccountStat = accountstat.ID
      account.ID_AccountInfo = accountinfo.ID
      Session.add(account)
      Session.flush()
      return [True, account]
   except Exception as e:
      return [False, str(e)]
  

def InsertVehicleSupportTable():
    TruncateTables({"VEHICLEBRAND", "VEHICLELINEUP", "VEHICLETYPE", "VEHICLECONDITION", "COLOR"})
    vehiclebrand_table = pd.read_csv(INITIALDATA + 'VehicleBrand.csv', index_col=False)
    vehiclelineup_table = pd.read_csv(INITIALDATA + 'VehicleLineup.csv', index_col=False)
    vehicletype_table = pd.read_csv(INITIALDATA + 'VehicleType.csv', index_col=False)
    color_table = pd.read_csv(INITIALDATA + 'Color.csv', index_col=False)
    vehiclecondition_table = pd.read_csv(INITIALDATA + 'VehicleCondition.csv', index_col=False)
    Session = new_Scoped_session()
    try:
        logolist = Session.query(Image).filter(Image.ID_ImageType==2).all()
        for item in logolist:
            Session.delete(item)
        Session.flush()
        for table in [vehiclebrand_table, vehicletype_table, color_table, vehiclecondition_table, vehiclelineup_table]:
            for i, row in table.iterrows():
                if table is vehiclebrand_table: 
                    image_url = row['logo']
                    output = SaveImageFromURL(Session=Session, url=image_url, image_type=2)
                    if output[0]:
                        new_row = VehicleBrand(ID=row['id'], Name=row['name'], ID_Image=output[1])
                    else: 
                        new_row = VehicleBrand(ID=row['id'], Name=row['name'])
                elif table is vehicletype_table: 
                    new_row = VehicleType(ID=row['id'], Type=row['name'])
                elif table is color_table:
                    new_row = Color(ID=row['id'], Name=row['name'], Color_hex=row['color_code'])
                elif table is vehiclecondition_table:
                    new_row = VehicleCondition(ID=row['id'], Condition=row['name'])
                else: 
                    new_row = VehicleLineup(ID=row['id'], Lineup=row['name'], ID_VehicleBrand=row['brand_id'])
                Session.add(new_row)
            Session.flush()
        Session.commit()
        return "Insert completed"
    except Exception as e:
        Session.rollback()
        return "Error: " + str(e)
    
    
def InsertTestAccounts():
    Session = new_Scoped_session()
    try:
        oldtestusers = Session.query(Account).filter(Account.Account_type==3).all()
        for i in oldtestusers:
            Session.remove(i)
        Session.flush()
        acc_list = []
        accinfo_list = []
        for i in range(5):
            output = SetupAccount(Session, f"testuser{i}@email.com", f"testuser{i}", "testuserpassword", 3, 4, f"Mobike Testuser {i}", "0123456789", None)
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
    
    
# def InsertTestPosts():
#     # TruncateTables({"VEHICLEINFO", "POST"})
#     post_table = pd.read_csv('Post.csv', index_col=False)
#     vehicleinfo_table = pd.read_csv('VehicleInfo.csv', index_col=False)
#     Session = new_Scoped_session()
#     try:
#         output = InsertTestAccounts()
#         if output["msg"] == "Completed":
#             acc_list = output["acc_list"]
#             for index, row in vehicleinfo_table.iterrows():
#                 new_VehicleInfo = VehicleInfo(ID=row['infoid'])
#             # UNFINISHED
#         Session.commit()
#         return "Insert completed"
#     except Exception as e:
#         Session.rollback()
#         return "Error: " + str(e)
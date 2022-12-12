# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:14:04 2022

@author: Karthik
"""

import pymongo
import pandas as pd
import json
import numpy as np
import xml.etree.ElementTree as ETree
xmldata="D:\\NCI Modules\\Sem 1\\DAP\\airports_list.xml"


client = pymongo.MongoClient("mongodb://localhost:27017")
df2 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\airport_weather_2019.csv")


df7 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_01.csv")
df8 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_02.csv")
df9 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_03.csv")
df10 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_04.csv")
df11 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_05.csv")
df12 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_06.csv")
df13 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_07.csv")
df14 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_08.csv")
df15 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_09.csv")
df16 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_10.csv")
df17 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_11.csv")
df18 = pd.read_csv("D:\\NCI Modules\\Sem 1\\DAP\\Project\\Dataset\\raw_data\\ONTIME_REPORTING_12.csv")

prstree = ETree.parse(xmldata)
root = prstree.getroot()



airportlist = []

all_data1 = []

for x in root.iter('row'):
    originid = x.find('ORIGIN_AIRPORT_ID').text
    airportname = x.find('DISPLAY_AIRPORT_NAME').text
    cityname = x.find('ORIGIN_CITY_NAME').text
    name = x.find('NAME').text

    airportlist = [ originid, airportname, cityname, name]
    all_data1.append(airportlist)

df23 = pd.DataFrame(all_data1, columns =['ORIGIN_AIRPORT_ID', 'DISPLAY_AIRPORT_NAME','ORIGIN_CITY_NAME','NAME'])


data7 = df7.to_dict(orient="records")
data8 = df8.to_dict(orient="records")
data9 = df9.to_dict(orient="records")
data10 = df10.to_dict(orient="records")
data11 = df11.to_dict(orient="records")
data12 = df12.to_dict(orient="records")
data13 = df13.to_dict(orient="records")
data14 = df14.to_dict(orient="records")
data15 = df15.to_dict(orient="records")
data16 = df16.to_dict(orient="records")
data17 = df17.to_dict(orient="records")
data18 = df18.to_dict(orient="records")

data2 = df2.to_dict(orient="records")

db = client["AirlineData"]
db.ONTIME_REPORTING_01.insert_many(data7)
db.ONTIME_REPORTING_02.insert_many(data8)
db.ONTIME_REPORTING_03.insert_many(data9)
db.ONTIME_REPORTING_04.insert_many(data10)
db.ONTIME_REPORTING_05.insert_many(data11)
db.ONTIME_REPORTING_06.insert_many(data12)
db.ONTIME_REPORTING_07.insert_many(data13)
db.ONTIME_REPORTING_08.insert_many(data14)
db.ONTIME_REPORTING_09.insert_many(data15)
db.ONTIME_REPORTING_10.insert_many(data16)
db.ONTIME_REPORTING_11.insert_many(data17)
db.ONTIME_REPORTING_12.insert_many(data18)

db.airport_weather_2019.insert_many(data2)
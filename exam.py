# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:04:34 2022

@author: ADMIN
"""

import xml.etree.ElementTree as ETree

import pandas as pd
import numpy as np
xmldata='C:\\Users\\ADMIN\\Desktop\\dona\\flights.xml'
prstree = ETree.parse(xmldata)
root = prstree.getroot()
# print(root)
temp = []
temp1 = []
all_items = []
dest_items = []
flightlist = prstree.findall('flight/origin')
i=0
for user in flightlist:
    name=user.find('name').text
    city=user.find('city').text
    fl_id=user.get("id")
    country=user.find('country').text
    iata_code=user.find('iata_code').text
    latitude=user.find('latitude').text
    longitude=user.find('longitude').text
    elevation=user.find('elevation').text
    temp = [ fl_id,name, city,country,iata_code,latitude,longitude,elevation]
    all_items.append(temp)
destlist = prstree.findall('flight/destination')
for user in destlist:
    fl_id=user.get("id")
    name=user.find('name').text
    city=user.find('city').text
    country=user.find('country').text
    iata_code=user.find('iata_code').text
    latitude=user.find('latitude').text
    longitude=user.find('longitude').text
    elevation=user.find('elevation').text
    temp1 = [ fl_id,name, city,country,iata_code,latitude,longitude,elevation]
    dest_items.append(temp1)

airlist_items=[]
airclist = prstree.findall('flight/aircraft')
i=0
for user in airclist:
    callsign=user.get("callsign")
    name=user.find('name').text
    manufacturer=user.find('manufacturer').text
    model=user.find('model').text
    numberofengines=user.find('numberofengines').text
    enginetype=user.find('enginetype').text
    idl=i
    i=i+1

    temp2 = [ callsign,name,manufacturer, model,numberofengines,enginetype,idl]
    airlist_items.append(temp2)

airclist_opr_items=[]
airclist_opr = prstree.findall('flight/aircraft/operator')
j=0
temp3=[]
for user in airclist_opr:
    name=user.find('name').text
    callsign=user.find('callsign').text
    iata_code=user.find('iata_code').text
    icao_code=user.find('icao_code').text
    country=user.find('country').text
    idl=j
    j=j+1
    temp3 = [name,callsign,iata_code, icao_code,country,idl]
    airclist_opr_items.append(temp3)
    
st=np.concatenate([airlist_items,airclist_opr_items],axis=1).tolist()


dep_opr_items=[]
dep_opr = prstree.findall('flight/departure')
temp4=[]
for user in dep_opr:
    scheduled=user.find('scheduled').text
    actual=user.find('actual').text
    temp4 = [scheduled,actual]
    dep_opr_items.append(temp4)

arri_opr_items=[]
arri_opr = prstree.findall('flight/departure')
temp5=[]
for user in arri_opr:
    scheduled=user.find('scheduled').text
    actual=user.find('actual').text
    temp5 = [scheduled,actual]
    arri_opr_items.append(temp5)
   
    
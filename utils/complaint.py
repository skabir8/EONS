import requests
import os
import sqlite3
import datetime

DIR=os.path.dirname(os.path.realpath(__file__))
DIR+='/../static/complaints.db'



def getCoords(address):
    data = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=AIzaSyBaKfjEKjJYrAX1paxoXt-tvv72KICf1bU")
    coords = data.json()["results"][0]["geometry"]["location"]
    return str(coords['lat']) + ',' + str(coords['lng'])

def addComplaint(complaint,address):
    db = sqlite3.connect(DIR)
    c = db.cursor()
    c.execute("INSERT INTO bronx (complaint, coord, cdate) VALUES (?,?,?)",
    (complaint, getCoords(address), datetime.datetime.now()))
    db.commit()
    db.close()
    return "Complaint Submitted"

def getComplaint(borough):
    db = sqlite3.connect(DIR)
    c = db.cursor()
    c.execute("SELECT * FROM " + borough)
    comps = c.fetchall()
    db.close()
    print comps

getComplaint('bronx')

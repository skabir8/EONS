import requests
import os
import sqlite3
import datetime

DIR=os.path.dirname(os.path.realpath(__file__))
DIR+='/../static/complaints.db'

db = sqlite3.connect(DIR)
c = db.cursor()

def getCoords(address):
    data = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=AIzaSyCrIErnSCAoA07R_m9NqNIQNcuD0Cf3Vn4")
    coords = data.json()["results"][0]["geometry"]["location"]
    return str(coords['lat']) + ',' + str(coords['lng'])

def addComplaint(complaint,address):
    c.execute("INSERT INTO bronx (complaint, coord, cdate) VALUES (?,?,?)",
    (complaint, getCoords(address), datetime.datetime.now()))
    db.commit()
    return "Complaint Submitted"

def getComplaint(borough):
    c.execute("SELECT * FROM " + borough)
    comps = c.fetchall()
    print comps
    
getComplaint('bronx')

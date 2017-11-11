import sqlite3

import os

def makeDB():
    DIR=os.path.dirname(os.path.realpath(__file__))
    DIR+='/../static/complaints.db'
    print DIR
    db=sqlite3.connect(DIR)
    c=db.cursor()
    q="CREATE TABLE bronx( \'complaint\' text, \'coord\' text, \'cdate\' text)"
    c.execute(q)
    q="CREATE TABLE brooklyn( \'complaint\' text, \'coord\' text, \'cdate\' text)"
    c.execute(q)
    q="CREATE TABLE queens( \'complaint\' text, \'coord\' text, \'cdate\' text)"
    c.execute(q)
    q="CREATE TABLE manhatten( \'complaint\' text, \'coord\' text, \'cdate\' text)"
    c.execute(q)
    q="CREATE TABLE statenisland( \'complaint\' text, \'coord\' text, \'cdate\' text)"
    c.execute(q)
    db.commit()
    db.close()

makeDB()

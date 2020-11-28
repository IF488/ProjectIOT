#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  appDhtWebServer.py
#  
#  Created by MJRoBot.org 
#  10Jan18

'''
	RPi Web Server for DHT captured data  
'''

from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime
import time

mydb = mysql.connector.connect(
host="***************",
user="*************",
password="***************",
database="**************"
)

mycursor = mydb.cursor()

app = Flask(__name__)

def gettemphum():
    temphum = "select * from temperaturedata order by id DESC LIMIT 1"
    mycursor.execute(temphum)
    mytemphum = mycursor.fetchall()
    mytime = []
    for x in mytemphum:
        mytime.append(x[0])
        mytemp = x[1]
        myhum = x[2]
    return mytemp, myhum
        

def getCOSmoke():
    sqlCOSmoke = "select * from airdata order by id DESC LIMIT 1"
    mycursor.execute(sqlCOSmoke)
    myCOSmoke = mycursor.fetchall()
    mytime = []
    for x in myCOSmoke:
        mytime.append(x[0])
        myCO = x[1]
        mySmoke = x[2]
    return myCO, mySmoke

def getnoise():
    sqlnoise = "select * from noisedata order by id DESC LIMIT 1"
    mycursor.execute(sqlnoise)
    mynoise = mycursor.fetchall()
    mytime = []
    for x in mynoise:
        mytime.append(x[0])
        mynoiselevel = str(x[1])
    return mynoiselevel


def getgraphtemp():
    sqlgraph = "select * from temperaturedata order by id DESC LIMIT 15"
    mycursor.execute(sqlgraph)
    myvalues = mycursor.fetchall()
    mytime = []
    graphvalues = []
    for x in myvalues:
        str(mytime.append(x[0]))
        graphvalues.append(x[1])
    return mytime, graphvalues
    
 
def getgraphhum():
    sqlgraph = "select * from temperaturedata order by id DESC LIMIT 15"
    mycursor.execute(sqlgraph)
    myvalues = mycursor.fetchall()
    mytime = []
    graphvalues = []
    for x in myvalues:
        str(mytime.append(x[0]))
        graphvalues.append(x[2])
    return mytime, graphvalues

def getgraphco():
    sqlgraph = "select * from airdata order by id DESC LIMIT 15"
    mycursor.execute(sqlgraph)
    myvalues = mycursor.fetchall()
    mytime = []
    graphvalues = []
    for x in myvalues:
        str(mytime.append(x[0]))
        graphvalues.append(x[1])
    return mytime, graphvalues

def getgraphsmoke():
    sqlgraph = "select * from airdata order by id DESC LIMIT 15"
    mycursor.execute(sqlgraph)
    myvalues = mycursor.fetchall()
    mytime = []
    graphvalues = []
    for x in myvalues:
        str(mytime.append(x[0]))
        graphvalues.append(x[2])
    return mytime, graphvalues

global location
location = 'C de Flacq'

app = Flask(__name__)

# main route 
@app.route("/home")
@app.route("/")
@app.route("/index")
def index():
    mytemp, myhum = gettemphum()
    myCO, mySmoke = getCOSmoke()
    mynoiselevel = getnoise()
    mylocation = location
    templateData = {
        'location'  : mylocation,
        'noise'  : mynoiselevel,
        'temperature'	: mytemp,
        'humidity'		: myhum,
        'CO'  : myCO,
        'Smoke'  : mySmoke
    }
    return render_template('main.html', **templateData)

@app.route('/Graph_mode', methods=['GET','POST'])
def Graph_mode():
    sensor = 'temperature'
    mytime, graphvalues = getgraphtemp()
    mylocation = location
    if request.method == 'POST':
        sensor = request.form['sens']
        if sensor == 'temperature':
             mytime, graphvalues = getgraphtemp()        
        elif sensor == 'humidity':
            mytime, graphvalues = getgraphhum()
        elif sensor == 'CO':
            mytime, graphvalues = getgraphco()
        elif sensor == 'smoke':
            mytime, graphvalues = getgraphsmoke()
    title = str(sensor)
    return render_template('template.html', title=title, location=mylocation, max=25, labels=mytime, values=graphvalues)

@app.route("/info")
def info():
    return render_template('info.html')

if __name__ == "__main__":
   app.run(host='192.168.43.128', port=5001, debug=True)


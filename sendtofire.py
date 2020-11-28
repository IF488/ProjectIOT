
from pyrebase import pyrebase
import mysql.connector
import time


firebaseConfig = {
   "apiKey": "**************************",
    "authDomain": "******************************",
    "databaseURL": "*******************************",
    "projectId": "****************************",
    "storageBucket": "***************************",
    "messagingSenderId": "**************************",
    "appId": "*************************************"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

mydb = mysql.connector.connect(
host="*************",
user="*************",
password="*************",
database="***************"
)

mycursor = mydb.cursor()

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



if __name__ == "__main__":
    while(True):
        temp, humid = gettemphum()
        myCO, mySmoke = getCOSmoke()
        mynoiselevel = getnoise()
        db.child("location").child("C de Flacq").update({'loctemperature': temp, 'lochumidity': humid, 'locair': myCO, 'locsmoke': mySmoke, 'locnoise': mynoiselevel})
        print("Data sent")
        time.sleep(20)





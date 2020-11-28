from mq import *
import sys, time
import mysql.connector
import datetime

mydb = mysql.connector.connect(host="*******", user="********", password="********", database="************")

mycursor = mydb.cursor()

try:
    print("Press CTRL+C to abort.")
    
    mq = MQ()
    while True:
        perc = mq.MQPercentage()
        lpg = perc["GAS_LPG"]
        co = perc["CO"]
        smoke = perc["SMOKE"]
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm" % (lpg, co, smoke))
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        mycursor.execute("INSERT INTO airdata (dateandtime, coperc, smokeperc) VALUES (%s, %s, %s)",(date, co, smoke))
        mydb.commit()
        sys.stdout.flush()
        time.sleep(900)

except:
    print("\nAbort by user")
    mycursor.close
    mydb.close()
    
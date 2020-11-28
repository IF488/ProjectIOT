#!/usr/bin/env python3
#############################################################################

import RPi.GPIO as GPIO
import time
import mysql.connector
import datetime
import Freenove_DHT as DHT

mydb = mysql.connector.connect(host="*********", user="**********", password="*********", database="************")

mycursor = mydb.cursor()

DHTPin = 11     #define the pin of DHT11

def loop():
    dht = DHT.DHT(DHTPin)   #create a DHT class object
    sumCnt = 0              #number of reading times 
    while(True):
        sumCnt += 1         #counting number of reading times
        chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        humid = dht.humidity
        temp = dht.temperature
        print ("The sumCnt is : %d, \t chk    : %d"%(sumCnt,chk))
        if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            print("DHT11,OK!")
            unix = int(time.time())
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
            mycursor.execute("INSERT INTO temperaturedata (dateandtime, temperature, humidity) VALUES (%s, %s, %s)",(date, temp, humid))
            mydb.commit()
        elif(chk is dht.DHTLIB_ERROR_CHECKSUM): #data check has errors
            print("DHTLIB_ERROR_CHECKSUM!!")
        elif(chk is dht.DHTLIB_ERROR_TIMEOUT):  #reading DHT times out
            print("DHTLIB_ERROR_TIMEOUT!")
        else:               #other errors
            print("Other error!")
            
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(humid, temp))
        time.sleep(300)       
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        mycursor.close
        mydb.close()
        GPIO.cleanup()
        exit()  


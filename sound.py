import RPi.GPIO as GPIO
import time
import mysql.connector
import datetime

mydb = mysql.connector.connect(host="*********", user="**********", password="**********", database="*************")

mycursor = mydb.cursor()

channel = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    while(True):
        if GPIO.input(channel):
            Noise = "HIGH"
            print(Noise)
        else:
            Noise = "LOW"
            print(Noise) 
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        mycursor.execute("INSERT INTO noisedata (dateandtime, level) VALUES (%s, %s)",(date, Noise))
        mydb.commit()
        time.sleep(10)

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=1000)
GPIO.add_event_callback(channel, callback)

while(True):
    time.sleep(1)

if __name__ == '__main__':
    try:
        callback()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        mycursor.close
        mydb.close()
        exit()
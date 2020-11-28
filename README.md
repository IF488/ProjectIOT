# IoT Project on Air and Noise pollution monitoring 
This repository contains the different files and folders for my IoT project on Air and Noise pollution. The project aims at sending data from the air and noise pollution sensors to a Web app and a Mobile app.

### DHT11 folder
This folder contains the executable file 'DHT11.py' and the required libraries for the DHT11 sensor. This program read temperature and humidity data from the sensor and send it to a MySQL database. 

### Gas-Sensor-MQ2
This folder contains the executable file 'MQ2.py' and the required libraries for the DHT11 sensor. This program read CO and smoke data from the sensor and send it to a MySQL database. 

### flaskWebsite
This folder contains the required file for my web app. The executable file is 'appDhtWebServer.py'. The templates folder contain the html files, and the static folder contains the css, javascript and images.

### sendtofire.py
This file send the last data from the MySQl database to my Firebase Realtime database which is used by my Mobile app.

### sound.py
This python program retrieve the data from the noise sensor and send it to my MySQl database.


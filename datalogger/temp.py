# Script based on information from https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ and other sources
#
# The script writes logs to three files:
#    temp.log:     Complete temperature log, with datetime, temperature and humidity. CSV format to save space
#    errors.log:   Errors reading the sensor are logged here
#    data.json:    The last entry as JSON
#    
# Released under MIT license to https://github.com/LB4FH/Templogger 
# Usage: /usr/bin/python3 temp.py


import Adafruit_DHT
import time
import datetime
import json

DT = datetime.datetime.now().isoformat()

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

if humidity is not None and temperature is not None:
    with open ("/home/pi/temp.log","a") as f:
        f.write("{0};{1:0.1f};{2:0.1f}\n".format(DT, temperature, humidity))
    data = {}
    data['last'] = []
    data['last'].append({
        'Temperature': round(temperature,2),
        'Humidity': round(humidity,2),
        'Timestamp': DT
    })
    with open ('data.json', 'w') as outfile:
        json.dump(data, outfile)
else:
    with open ("/home/pi/errors.log","a") as f:
        f.write("{0}\tFailed to read sensor\n".format(DT))
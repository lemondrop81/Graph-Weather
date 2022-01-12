from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/509944'

pages = 1
weather = get(url).json()
data = weather['items']

temperatures = [record['ambient_temp'] for record in data]
timestamps = [parser.parse(record['reading_timestamp']) for record in data]

airQuality = [record['air_quality'] for record in data]

humidity = [record['humidity'] for record in data]

plt.plot(timestamps, airQuality, label='Air Quality Index')
plt.plot(timestamps, temperatures, label='temp °c')
plt.plot(timestamps, humidity, label='humidity %')
plt.legend()
plt.show()
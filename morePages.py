from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/1682287'

pages = 1
weather = get(url).json()
data = weather['items']

# Loop through a months worth of data
while 'next' in weather and pages < 9:
    url = weather['next']['$ref']
    print('Fetching {0}'.format(url))
    weather = get(url).json()
    data += weather['items']
    pages += 1

# Assigns the timestamp data set to a variable
timestamps = [parser.parse(record['reading_timestamp']) for record in data]

# Assigns the ambient temperature data set to a value
temperatures = [record['ambient_temp'] for record in data]

# Assigns the air quality data set to a variable
airQuality = [record['air_quality'] for record in data]

# Assigns the humidity data set to a variable
humidity = [record['humidity'] for record in data]

# Plots the data sets 
plt.plot(timestamps, airQuality, label='Air Quality Index')
plt.plot(timestamps, temperatures, label='temp °c')
plt.plot(timestamps, humidity, label='humidity %')

# Display the label and legends
plt.xlabel('date and time')
plt.legend()
plt.show()
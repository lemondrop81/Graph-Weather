"""
    Assignment 2 Graphing the weather
    Date: January 12 2022
    Description: A simple program that graphs the weather
"""

from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/509944'

pages = 1
weather = get(url).json()
data = weather['items']

# Loop through a months worth of data
for i in range(20):
    url = f'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/509944?page={i}'
    print(url)
    weather = get(url).json()
    data += weather['items']

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
plt.xlabel('date')
plt.legend()
plt.show()
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/587328'

weather = get(url).json()

temperatures = [record['ambient_temp'] for record in weather['items']]
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]

## create a plot of timestamps against temperature and show it
plt.plot(timestamps, temperatures)
## Set the axis labels
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
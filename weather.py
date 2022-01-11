from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

# Web api to get the weather at the weather station
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/552355'

# save the data to a variable
weather = get(url).json()
#can you provide python code to read list of climatedata from http://localhost:1111/api/v1/climate url and plot chart with city and temperature for the month of January?
#Path: python/climatedata.py
#read list of climatedata from http://localhost:1111/api/v1/climate url

import requests
import json

url = "http://localhost:1111/api/v1/climate"
response = requests.get(url)
data = response.json()

#plot chart with city and temperature for the month of January
import matplotlib.pyplot as plt
import numpy as np

city = []
temperature = []

for i in range(len(data)):
    city.append(data[i]['city'])
    temperature.append(data[i]['temperature'])

y_pos = np.arange(len(city))
plt.bar(y_pos, temperature, align='center', alpha=0.5)
plt.xticks(y_pos, city)
plt.ylabel('Temperature')
plt.title('Temperature in January')
plt.show()
#
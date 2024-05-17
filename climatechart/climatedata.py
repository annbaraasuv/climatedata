# read list of climatedata from http://localhost:1111/api/v1/climate url

import requests
import json

url = "http://localhost:1111/api/v1/climate"
response = requests.get(url)
data = response.json()

# Filter data for the month of January
january_data = [d for d in data if d['month'] == 'January']

# Plot chart with city and temperature for the month of January
import matplotlib.pyplot as plt
import numpy as np

city = []
temperature = []

for i in range(len(january_data)):
    city.append(january_data[i]['city'])
    temperature.append(january_data[i]['temperature'])

y_pos = np.arange(len(city))
plt.bar(y_pos, temperature, align='center', alpha=0.5)
plt.xticks(y_pos, city)
plt.ylabel('Temperature')
plt.title('Temperature in January')
plt.show()




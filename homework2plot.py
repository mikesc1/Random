# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:19:58 2018

@author: Michael

Some basic graphing using numpy and matplotlib, long since lost weather_data.txt, sorry...
Good for learning how to read in text files and display 2 decimal places
"""
import numpy as np
import matplotlib.pyplot as plt

#weatherdata = open("weather_data(1).txt", "r")
#for line in weatherdata:
#    data = line.split(",");
#    UTC = data[0];
#    temperature = data[1]
#    humidity

UTC = np.loadtxt("weather_data(1).txt", delimiter=",", usecols=(0));
temperature = np.loadtxt("weather_data(1).txt", delimiter=",", usecols=(1));
humidity = np.loadtxt("weather_data(1).txt", delimiter=",", usecols=(2));

time = len(UTC);
sumtemp = 0;
sumhum = 0;

for i in temperature:
    sumtemp +=i;
for j in humidity:
    sumhum +=j;
    
averagetemp = sumtemp/time;
averagehum = sumhum/time;

lowtemperature = np.amin(temperature);
hightemperature = np.amax(temperature);

# Plot One

plt.plot(UTC,temperature)
plt.xlabel("Unix Time Stamp (seconds)")
plt.ylabel("Temperature (Celsius)")
plt.title("Temperature over Time")
plt.show()

print("The average temperature during this period was " + str('%.2f' % averagetemp) + " deg. C")
print("The highest recorded tempurature during this period is " + str(hightemperature) + " deg. C")
print("The lowest recorded tempurature during this period is " + str(lowtemperature) + " deg. C")

plt.plot(UTC,humidity)
plt.xlabel("Unix Time Stamp (seconds)")
plt.ylabel("Humidity %")
plt.title("Humidity over Time")
plt.show()

print("The average humidity during this period was " + str('%.2f' % averagehum) + " %")



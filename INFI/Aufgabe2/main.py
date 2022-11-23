from math import nan
import numpy as np
import matplotlib.pyplot as plt

#source: https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data
d = np.genfromtxt('INFI\Aufgabe2\data\london_weather.csv', delimiter=",", skip_header=1 )

dt =  d[:,0] #Datum mit folgendem Aufbau: 19790103 (3.Jänner 1979)
# Aufteilen in Tag, Monat, Jahr
day = (dt % 100).astype('i')
month = (dt % 10000 / 100).astype('i')
year = (dt % 100000000 / 10000).astype('i')

# Check ob es funktioniert hat
print("Jahr:", np.unique(year, return_counts=True))
print("Monat", np.unique(month, return_counts=True))
print("Tag:", np.unique(day, return_counts=True))
print("Jahr MIN MAX" , np.min(year), np.max(year))

sun = d[:,2] # Sonnenstunden

max_temp = d[:,4]

mean_temp = d[:,5] 

min_temp=d[:,6]

snow_depth = d[:,9]

mean_temp_1979 = mean_temp[year == 1979]

mean_temp_1989 = mean_temp[year == 1989]

mean_temp_1999 = mean_temp[year == 1999]

mean_temp_2009 = mean_temp[year == 2009]

mean_temp_2019 = mean_temp[year == 2019]

#Da nan-werte in der datei vorzufinden sind, muss man diese herausfiltern
mean_temp_20092 = mean_temp_2009[~np.isnan(mean_temp_2009)]

mean_temp_20192 = mean_temp_2019[~np.isnan(mean_temp_2019)]

# Darstellung der Temperaturunterschiede
plt.boxplot([mean_temp_1979, mean_temp_1989, mean_temp_1999, mean_temp_20092, mean_temp_20192])
plt.xlabel("Jahr")
plt.xticks([1,2,3,4,5], ["1979", "1989", "1999", "2009", "2019"])
plt.ylabel("Temperatur")
plt.savefig("INFI\Aufgabe2\pics\Task_1-1.png")
plt.show()

#1.2
plt.plot(mean_temp_20192, "r.")
plt.xlabel("Tag")
plt.ylabel("Temperatur")
plt.savefig("INFI\Aufgabe2\pics\Task_1-2.png")
plt.show()

#1.3
quant_1979 = np.quantile(mean_temp_1979, 0.5)

quant_1989 = np.quantile(mean_temp_1989, 0.5)

quant_1999 = np.quantile(mean_temp_1999, 0.5)

quant_2009 = np.quantile(mean_temp_20092, 0.5)

quant_2019 = np.quantile(mean_temp_20192, 0.5)

plt.plot(["1979", "1989", "1999", "2009", "2019"],[quant_1979, quant_1989, quant_1999, quant_2009, quant_2019])
plt.xlabel("Jahr")
plt.ylabel("Extremwert der Temperatur")
plt.savefig("INFI\Aufgabe2\pics\Task_1-3.png")
plt.show()

#1.4
years = []
temps = []

for i in range(2011, 2020 + 1):
    years.append(str(i))
    temp = mean_temp[year == i]
    temp2 = temp[~np.isnan(temp)]
    temp2_mean = np.mean(temp2)
    temps.append(temp2_mean)

plt.bar(years, temps, align='center')
plt.xlabel("Jahr")
plt.xticks([0,1,2,3,4,5,6,7,8,9], ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"])
plt.ylabel("Temperatur")
plt.savefig("INFI\Aufgabe2\pics\Task_1-4.png")
plt.show()

#1.5
years = []
rads = []

for i in range(2011, 2020 + 1):
    years.append(str(i))
    snow = snow_depth[year == i]
    snow2 = snow[~np.isnan(snow)]
    snow2_mean = np.mean(snow2)
    rads.append(snow2_mean)

plt.bar(years, rads, align='center')
plt.xlabel("Jahr")
plt.xticks([0,1,2,3,4,5,6,7,8,9], ["2011", "2012", "2013", "2014", "2015", "2016", "2017","2018", "2019", "2020"])
plt.ylabel("Mittelwert der globalen Schneetiefe")
plt.savefig("INFI\Aufgabe2\pics\Task_1-5.png")
plt.show()
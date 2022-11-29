import numpy as np
import pandas as pa
import seaborn as se
from matplotlib import pyplot as pyp

dataStays = pa.read_excel("INFI\Aufgabe3\data\Zeitreihe-Winter-2022092012.xlsx")

baseStays = ['Bezirk','Gemnr','Gemeinde']
yearsStays = dataStays.columns[3:].astype(str)
baseStays.extend('x' + yearsStays)
dataStays.columns = baseStays

#Task 2.1
growthIbk = dataStays.values[2,3:]
pyp.title("Nächtigungen in Ibk")
pyp.plot(growthIbk, "m.")
pyp.xlabel("Jahr")
pyp.ylabel("Anz. Nächigungen")
pyp.savefig("INFI\Aufgabe3\pics\Task_2-1.png")
pyp.show()

#Task 2.2
gem = dataStays[dataStays.Bezirk == "KU"]
growthDist = gem[dataStays.columns[0:]].values[:,3:].sum(axis=0)
print(growthDist)
pyp.title("Nächtigungen in Bezirk Kufstein")
pyp.plot(growthDist, "m-")
pyp.xlabel("Jahr")
pyp.ylabel("Anz. Nächigungen")
pyp.savefig("INFI\Aufgabe3\pics\Task_2-2.png")
pyp.show()

#Task 3.1
minArr = []
maxArr = []
rangeArr = []
avgArr = []
for i in range(278):
    minimum = min(dataStays.values[i,3:])
    maximum = max(dataStays.values[i,3:])
    ranges = maximum-minimum
    average = dataStays.values[i,3:].mean()
    minArr.append(minimum)
    maxArr.append(maximum)
    rangeArr.append(ranges)
    avgArr.append(average)

dataStays["minimum"] = minArr
dataStays["maximum"] = maxArr
dataStays["range"] = rangeArr
dataStays["avg"] = avgArr

#Task 3.1.1
standardRange = []
for i in range(len(rangeArr)):
    standardRange.append(rangeArr[i]/avgArr[i])

dataStays["standardRange"] = standardRange

#Task 3.2
touristsPerYear = dataStays[dataStays.columns[3:]].values[1:,:].sum(axis=0)
print("Touristen pro Jahr:")
print(touristsPerYear)
print("____________________")
touristsOverall = np.sum(touristsPerYear)
print("Touristen gesamt:")
print(touristsOverall)
print("____________________")
print("Touristen gesamt pro Bezirk:")
allDistricts = ["I", "IM", "IL", "KB", "KU", "LA", "LZ", "RE", "SZ"]
touristsOverallPerDist = []
for i in range(len(allDistricts)):
    touristsOverallPerDist.append(dataStays[dataStays.Bezirk == allDistricts[i]].values[:,3:].sum())
print(touristsOverallPerDist)

#Task 4.1
#a
#dataStays.boxplot(column="standardRange", by="Bezirk")

#b
#pos = 0
#labels = dataStays['Bezirk'].unique()
#for b in labels:
#    bez = dataStays[dataStays.Bezirk == b]
#    pyp.boxplot(bez['standardRange'], positions=[pos])
#    pos += 1
#    pyp.xticks(range(len(labels)), labels)

#c
se.boxplot(x=dataStays['Bezirk'], y=dataStays['standardRange'], data=dataStays)

pyp.savefig("INFI\Aufgabe3\pics\Task_4-1.png")
pyp.show()

#Task 4.2
se.barplot(x=dataStays.columns[3:26], y=dataStays.values[2,3:26], palette='terrain')
pyp.show()

#Task 5
dataPop = pa.read_excel("INFI\Aufgabe3\data/bev_meld.xlsx")

data = pa.merge(dataStays, dataPop, how='inner', on='Gemnr')
data = data.drop(columns='Gemnr')

base = ['Bezirk','Gemeinde']
years = data.columns[2:25].astype(str)
base2 = ['minimum', 'maximum', 'range', 'avg', 'standardRange', 'Bezirk2', 'Gemeinde2']
years2 = data.columns[32:].astype(str)
base.extend(years)
base.extend(base2)
base.extend('y' + years2)
data.columns = base

#a
staysPerPerson_2018 = data['x2018']/data['y2018']
staysPerPerson_2020 = data['x2020']/data['y2020']

#b
#Manche Bezirke haben bei weitem mehr Zouristen auf die Gesamteinwohnerzahl
#als weniger touristenreiche Bezirke

#Zusätzlich sind in manchen Bezirken einige Gemeinde bei weitem beliebter, daher ist bei dem jeweiligem Boxplot
#auch eine größere Differenz vorzufinden
se.boxplot(x=data['Bezirk'], y=staysPerPerson_2018, data=data)
pyp.savefig("INFI\Aufgabe3\pics\Task_5-b-1.png")
pyp.show()

se.boxplot(x=data['Bezirk'], y=staysPerPerson_2020, data=data)
pyp.savefig("INFI\Aufgabe3\pics\Task_5-b-2.png")
pyp.show()

#c
lowestTen = staysPerPerson_2020.sort_values(ascending=True)
highestTen = staysPerPerson_2020.sort_values(ascending=False)

lowestIndexes = []
highestIndexes = []
districts = data['Gemeinde']
for i in range(0,10):
    lowestIndexes.append(districts[lowestTen.index[staysPerPerson_2020 == lowestTen[i]]].values[0])
    highestIndexes.append(districts[highestTen.index[staysPerPerson_2020 == highestTen[i]]].values[0])

se.boxplot(x=lowestIndexes, y=lowestTen[:10], data=data)
pyp.savefig("INFI\Aufgabe3\pics\Task_5-c-1.png")
pyp.show()

se.boxplot(x=highestIndexes, y=highestTen[:10], data=data)
pyp.savefig("INFI\Aufgabe3\pics\Task_5-c-2.png")
pyp.show()

#d
pyp.title("Nächtigungen pro Kopf in Wörgl")
pyp.plot(staysPerPerson_2020[136], "m.")
pyp.xlabel("Gemeinde")
pyp.ylabel("Anz. Nächigungen pro Kopf")
pyp.savefig("INFI\Aufgabe3\pics\Task_5-d.png")
pyp.show()
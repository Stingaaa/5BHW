import random

arrZiehung = []
dictStatistics = {}
minVal = 0
maxVal = 0

def initArr():
    global arrZiehung
    arrZiehung = []
    x = 0
    while x < maxVal:
        x += 1
        arrZiehung.append(x)
        
def initStatistics():
    x = minVal-1
    while x < maxVal:
        x += 1
        dictStatistics[x] = 0
        
def printZiehung():
    x = 0
    while x < 6:
        x += 1
        if(x < 6):
            print(arrZiehung[len(arrZiehung)-x], end = " - ")
        else:
            print(arrZiehung[len(arrZiehung)-x])
        
def printStatistics():
    print(dictStatistics)
        
def ziehungen(anz):
    while anz > 0:
        initArr()
        anz -= 1
        x = 0
        while x < 6:
            x+=1
            rand = random.randint(minVal, maxVal)
            arrZiehung[len(arrZiehung)-x], arrZiehung[rand-1] = arrZiehung[rand-1], arrZiehung[len(arrZiehung)-x]
            dictStatistics[rand] = dictStatistics[rand] + 1


minVal = int(input("Min: "))
maxVal = int(input("Max: "))
initStatistics()
        
print("Einfache Ziehung:")
ziehungen(1)
printZiehung()

anzZiehungen = input("Wie oft soll gezogen werden: ")
print(anzZiehungen + " Ziehungen:")
ziehungen(int(anzZiehungen))
printStatistics()
import random

arrZiehung = []
dictStatistics = {}

def initArr():
    global arrZiehung
    arrZiehung = []
    x = 0
    while x < 45:
        x += 1
        arrZiehung.append(x)
        
def initStatistics():
    x = 0
    while x < 45:
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
    
    
def Ziehungen(anz):
    while anz > 0:
        initArr()
        anz -= 1
        x = 0
        while x < 6:
            x+=1
            rand = random.randint(1, 45)
            arrZiehung[len(arrZiehung)-x], arrZiehung[rand-1] = arrZiehung[rand-1], arrZiehung[len(arrZiehung)-x]
            if(anz > 0):
                dictStatistics[rand] = dictStatistics[rand] + 1
        
print("Einfache Ziehung:")
Ziehungen(1)
printZiehung()

initStatistics()
anzZiehungen = input("Wie oft soll gezogen werden: ")
print(anzZiehungen + " Ziehungen:")
Ziehungen(int(anzZiehungen))
printStatistics()
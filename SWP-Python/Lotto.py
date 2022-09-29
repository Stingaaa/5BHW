import random

def initArr():
    arrZiehung = []
    for x in range(minVal, maxVal+1):
        arrZiehung.append(x)
    return arrZiehung
        
def initStatistics():
    dictStatistics = {}
    for x in range(minVal, maxVal+1):
        dictStatistics[x] = 0
    return dictStatistics
        
def printZiehung(arr):
    for x in range(1,7):
        if(x < 6):
            print(arr[len(arr)-x], end = " - ")
        else:
            print(arr[len(arr)-x])
        
def printStatistics(dict):
    print(dict)
        
def ziehungen(anz, arr, dict):
    for i in range(anz):
        for x in range(1,7):
            rand = random.randint(minVal, maxVal)
            arr[len(arr)-x], arr[rand-minVal-1] = arr[rand-minVal-1], arr[len(arr)-x]
            dict[rand] = dict[rand] + 1
    if anz == 1:
        return arr 
    return dict

if __name__ == '__main__':

    minVal = int(input("Minimum Value: "))
    maxVal = int(input("Maximum Value: "))
    
    print("Einfache Ziehung:")
    printZiehung(ziehungen(1, initArr(), initStatistics()))

    anzZiehungen = input("Wie oft soll gezogen werden: ")
    print(anzZiehungen + " Ziehungen:")
    printStatistics(ziehungen(int(anzZiehungen), initArr(), initStatistics()))
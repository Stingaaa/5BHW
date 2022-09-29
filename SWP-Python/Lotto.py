import random

def initArr(minV, maxV):
    arrZiehung = []
    for x in range(minV, maxV+1):
        arrZiehung.append(x)
    return arrZiehung
        
def initStatistics(minV, maxV):
    dictStatistics = {}
    for x in range(minV, maxV+1):
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
        
def ziehungen(minV, maxV, anz, arr, dict):
    for i in range(anz):
        for x in range(1,7):
            rand = random.randint(minV, maxV)
            arr[len(arr)-x], arr[rand-minV-1] = arr[rand-minV-1], arr[len(arr)-x]
            dict[rand] += 1
    if anz == 1:
        return arr 
    return dict

if __name__ == '__main__':

    minVal = int(input("Minimum Value: "))
    maxVal = int(input("Maximum Value: "))
    
    print("Einfache Ziehung:")
    printZiehung(ziehungen(minVal, maxVal, 1, initArr(minVal, maxVal), initStatistics(minVal, maxVal)))

    anzZiehungen = input("Wie oft soll gezogen werden: ")
    print(anzZiehungen + " Ziehungen:")
    printStatistics(ziehungen(minVal, maxVal, int(anzZiehungen), initArr(minVal, maxVal), initStatistics(minVal, maxVal)))
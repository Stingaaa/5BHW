import random

def initArr(mM):
    arrZiehung = []
    for x in range(mM[0], mM[1]+1):
        arrZiehung.append(x)
    return arrZiehung
        
def initStatistics(mM):
    dictStatistics = {}
    for x in range(mM[0], mM[1]+1):
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
        
def ziehungen(mM, anz, arr, dict):
    for i in range(anz):
        print(arr)
        for x in range(1,7):
            rand = random.randint(mM[0], mM[1])
            arr[len(arr)-x], arr[rand-mM[0]-1] = arr[rand-mM[0]-1], arr[len(arr)-x]
            dict[rand] += 1
    if anz == 1:
        return arr 
    return dict

if __name__ == '__main__':

    minMax = int(input("Minimum Value: ")), int(input("Maximum Value: "))
    
    print("Einfache Ziehung:")
    printZiehung(ziehungen(minMax, 1, initArr(minMax), initStatistics(minMax)))

    anzZiehungen = input("Wie oft soll gezogen werden: ")
    print(anzZiehungen + " Ziehungen:")
    printStatistics(ziehungen(minMax, int(anzZiehungen), initArr(minMax), initStatistics(minMax)))
import math
import random

class Elem:
  # constructor
    def __init__(self, data = None, next=None): 
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

# A Linked List class with a single head node
class List:
    def __init__(self):  
        self.head = None

    def elemAtIndex(self, index):
        elem = self.head
        for i in range(index+1):
            if i == index and elem.data != None:
                return elem
            elem = elem.next
        return "Index out of range"
  
  # insertion method for the linked list
    def add(self, data):
        newElem = Elem(data)
        if self.head != None:
            l = len(self)
            lastElem = self.elemAtIndex(len(self)-1)
            if type(lastElem) == str:
                return lastElem
            lastElem.next = newElem
        else:
            self.head = newElem

    def insert(self, index, data):
        prevElem = self.elemAtIndex(index)
        elem = Elem(data)
        if type(elem) == str:
            print(elem)
        else:
            if index == 0:
                self.head = elem
            else:
                temp = self.elemAtIndex(index-1)
                temp.next = elem
            elem.next = prevElem
        
    def remove(self, elem):
        elemToDelete = self.elemAtIndex(self.index(elem))
        elemToDelete = elemToDelete.next
        elemToDelete.next = elemToDelete.next.next

    def removeIndex(self, index):
        self.remove(self[index])
        
    def __len__(self):
        l = 0
        nextElem = self.head
        while not nextElem == None:
            nextElem = nextElem.next
            l += 1
        return l
    
    def index(self, elem):
        i = 0
        temp = self.head
        while not temp.data == elem:
            temp = temp.next
            if temp == None:
                return
            i += 1
        return i

    def __getitem__(self, index):
        if type(index) == slice:
            items = List()
            if index.start < len(self):
                for i in range(index.start, index.stop if index.stop < len(self) else len(self)):
                    items.add(self[i])
                return items
            else:
                return None
        e = self.elemAtIndex(index)
        return e.data
    
    def __setitem__(self, index, val):
        e = self.elemAtIndex(index)
        e.data = val

    def sort(self, method="quick"):
        def merge(a, b):
            merged = List()
            if a == None and b == None:
                return merged
            elif a == None:
                merged = b if type(b) == List else merged.add(b)
                return merged
            elif b == None:
                merged = a if type(a) == List else merged.add(a)
                return merged
            elif type(a) != List and type(b) != List:
                if a > b:
                    merged.add(b)
                    merged.add(a)
                else:
                    merged.add(a)
                    merged.add(b)
                return merged
            elif type(a) != List:
                posB = 0
                b.add(int(math.pow(10, 100)))
                for i in range(len(b)):
                    if a > b[posB]:
                        merged.add(b[posB])
                        posB += 1
                    elif a < b[posB]:
                        merged.add(a)
                        a = Elem(int(math.pow(10, 100)))
            elif type(b) != List:
                posA = 0
                a.add(int(math.pow(10, 100)))
                for i in range(len(a)):
                    if a[posA] > b:
                        merged.add(a[posA])
                        posA += 1
                    elif a[posA] < b:
                        merged.add(b)
                        b = Elem(int(math.pow(10, 100)))
            else:
                posA, posB = 0, 0
                a.add(int(math.pow(10, 20))), b.add(int(math.pow(10, 20)))
                for i in range(len(a)+len(b)-2):
                    if a[posA] > b[posB]:
                        merged.add(b[posB])
                        posB += 1
                    else:
                        merged.add(a[posA])
                        posA += 1
                return merged


        match method:
            case "quick":
                for i in range(len(self)):
                    for j in range(i+1,len(self)):
                        if self[i].data > self[j].data:
                            self[i].data, self[j].data = self[j].data, self[i].data
                return self
            case "merge":
                l = len(self)
                cicles = int(math.log2(l)) if math.log2(l) == int(math.log2(l)) else int(math.log2(l))+1
                for i in range(0, cicles):
                    for j in range(int(l/((i+1)*2))-1 if l/(i+1)*2 == int(l/((i+1)*2)) else int(l/((i+1)*2))):
                        if(l >= j+1):
                            a = self[int(j*math.pow(2,i+1)) : int(j*math.pow(2,i+1)+2*int(math.pow(2,i-1))) + (1 if i == 0 else 0)]
                            b = self[int(j*math.pow(2,i+1)+2*int(math.pow(2,i-1))) + (1 if i == 0 else 0) : int(j*math.pow(2,i+1)+4*int(math.pow(2,i-1))) + (2 if i == 0 else 0)]
                            merged = merge(a, b)
                            for r in range(len(merged)):
                                self[int(j*math.pow(2,i+1))+r] = merged[r]
                return self
                    
    def split(self, parts):
        l = len(self)
        p = parts
        if parts > l:
            print("List only has ", l, " elements to split in it!")
            return
        splitLists = List()
        for i in range(parts):
            elemForPart = int(l/p)
            listPart = List()
            for j in range(len(self)-l,len(self)-l+elemForPart):
                listPart.add(self[j])
            splitLists.add(listPart)
            p -= 1
            l -= elemForPart
        return splitLists  
    
    def shuffle(self):
        for i in range(len(self)):
            rand = random.randint(0, len(self)-1)
            currPos = self[i]
            randPos = self[rand]
            self[i] = randPos
            self[rand] = currPos
        return self

    def getData(self):
        current = self.head
        info = "["
        while(current):
            if type(current.data) == List:
                info += current.data.getData() + ","
            else:
                info += str(current.data) + ","
            current = current.next
        info = info[:-1] + "]"
        return info

  # print method for the linked list
    def __str__(self):
        current = self.head
        info = "["
        while(current):
            if type(current.data) == List:
                info += current.data.getData() + ","
            else:
                info += str(current.data) + ","
            current = current.next
        info = info[:-1] + "]"
        return info
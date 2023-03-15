import math
import random

class Elem:
  # constructor
    def __init__(self, data = None, next=None, prev=None): 
        self.data = data
        self.next = next
        self.previous = prev

    def __str__(self):
        return str(self.data)

# A Linked List class with a single head node
class List:
    def __init__(self):  
        self.head = None
        self.last = None

    def elemAtIndex(self, index):
        elem = self.head
        for i in range(index):
            elem = elem.next
        return elem
  
  # insertion method for the linked list
    def add(self, data):
        newElem = Elem(data)
        if self.head == None:
            self.head = newElem
            self.last = newElem
        elif self.head.next == None:
            self.last = newElem
            self.head.next = self.last
            self.last.previous = self.head
        else:
            temp = self.last
            self.last = newElem
            self.last.previous = temp
            self.last.previous.next = newElem

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
        
    def remove(self, elem=None):
        if elem == None:
            self.last = self.last.previous
            self.last.previous.next = self.last
            self.last.next = None
        else:
            elemToDelete = self.elemAtIndex(self.index(elem))
            if elemToDelete.next == None:
                self.last = self.last.previous
                self.last.previous.next = self.last
                self.last.next = None
            else:
                elemToDelete = elemToDelete.previous
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
        
    def contains(self, val):
        e = self.head
        for i in range(len(self)):
            if e.data == val:
                return True
            e = e.next
        return False
    
    def find(self, val):
        e = self.head
        index = 0
        for i in range(len(self)):
            if e.data == val:
                return index
            e = e.next
            index += 1
        return None

    def sort(self, method="bubble"):
        def merge(arr, l, m , r):
            n1 = m - l + 1
            n2 = r - m
        
            L = [0] * (n1)
            R = [0] * (n2)
        
            for i in range(0, n1):
                L[i] = arr[l + i]
        
            for j in range(0, n2):
                R[j] = arr[m + 1 + j]
        
            i = 0     
            j = 0     
            k = l     
        
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
        
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1
        
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1
        
        def mergeSort(arr, l, r):
            if l < r:
                m = l+(r-l)//2
                mergeSort(arr, l, m)
                mergeSort(arr, m+1, r)
                merge(arr, l, m, r)

        list = self.merge()
        match method:
            case "bubble":
                for i in range(len(list)):
                    for j in range(i+1,len(list)):
                        if list[i] > list[j]:
                            list[i], list[j] = list[j], list[i]
                return list
            case "merge":
                l = len(list)
                mergeSort(list, 0, l-1)
                return list
            
    def sortMerge(self):
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
            
        list = self.merge()
        l = len(list)
        cicles = int(math.log2(l)) if math.log2(l) == int(math.log2(l)) else int(math.log2(l))+1
        for i in range(0, cicles):
            for j in range(int(l/((i+1)*2))-1 if l/(i+1)*2 == int(l/((i+1)*2)) else int(l/((i+1)*2))):
                if(l >= j+1):
                    a = list[int(j*math.pow(2,i+1)) : int(j*math.pow(2,i+1)+2*int(math.pow(2,i-1))) + (1 if i == 0 else 0)]
                    b = list[int(j*math.pow(2,i+1)+2*int(math.pow(2,i-1))) + (1 if i == 0 else 0) : int(j*math.pow(2,i+1)+4*int(math.pow(2,i-1))) + (2 if i == 0 else 0)]
                    merged = merge(a, b)
                    for r in range(len(merged)):
                        list[int(j*math.pow(2,i+1))+r] = merged[r]
        return list
                    
    def split(self, parts):
        l = len(self)
        p = parts
        if parts > l:
            print("List only has ", l, " elements to split in it!")
            return self
        if parts == 0:
            print("Cant split list into 0 parts!")
            return self
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
    
    def merge(self):
        list = List()
        for i in range(len(self)):
            if type(self[i]) == List:
                for j in range(len(self[i])):
                    list.add(self[i][j])
            else:
                list.add(self[i])
        return list
    
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
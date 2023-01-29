import math

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
  
  # insertion method for the linked list
    def add(self, data):
        newElem = Elem(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newElem
        else:
            self.head = newElem
        
    def remove(self, elem):
        elemToDelete = self.head
        if self.head.data == elem:
            self.head = self.head.next
            return
        while not elemToDelete.next.data == elem:
            elemToDelete = elemToDelete.next
            if elemToDelete.next == None:
                print("Couldnt remove")
                break
        elemToDelete.next = elemToDelete.next.next
        
    def __len__(self):
        l = 1
        nextElem = self.head
        while not nextElem.next == None:
            nextElem = nextElem.next
            l += 1
        return l
    
    def index(self, elem):
        i = 0
        temp = self.head
        while not temp == elem:
            temp = temp.next
            if temp == None:
                print("Element not found")
                break
            i += 1
        return i
    
    def getItems(self, a, b):
        items = List()
        if b >= len(self):
            b = len(self)
        if a == b or a+1 == b:
            return self[a]
        for i in range(int(a), int(b)):
            items.add(self[i].data)
        return items

    def __getitem__(self, index):
        e = self.head
        if index == -1:
            return e
        while not self.index(e) == index:
            e = e.next
            if e == None:
                print("Index out of range")
                break
        return e
    
    def sort(self, method="quick"):
        def merge(a, b):
            merged = List()
            if type(a) != List and type(b) != List:
                if a.data > b.data:
                    merged.add(b.data)
                    merged.add(a.data)
                else:
                    merged.add(b.data)
                    merged.add(a.data)
                print(merged)
                return merged
            elif type(a) != List:
                posB = 0
                b.add(int(math.pow(10, 100)))
                for i in range(len(b)+1):
                    if a.data > b[posB].data.data:
                        merged.add(b[posB])
                        posB += 1
                    elif a.data < b[posB].data.data:
                        merged.add(a)
                        a = Elem(int(math.pow(10, 100)))
            elif type(b) != List:
                posA = 0
                a.add(int(math.pow(10, 100)))
                for i in range(len(a)+1):
                    if a[posA].data.data > b.data:
                        merged.add(a[posA])
                        posA += 1
                    elif a[posA].data.data < b.data:
                        merged.add(b)
                        b = Elem(int(math.pow(10, 100)))
            else:
                posA, posB = 0, 0
                a.add(int(math.pow(10, 20))), b.add(int(math.pow(10, 20)))
                for i in range(len(a)+len(b)):
                    if a[posA].data > b[posB].data:
                        merged.add(b[posB])
                        posB += 1
                    elif a[posA].data < b[posB].data:
                        merged.add(a[posB])
                        posA += 1
                print(merged)
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
                for i in range(1, cicles+1):
                    for j in range(int(l/(i*2))-1 if l/i*2 == int(l/(i*2)) else int(l/(i*2))):
                        if(l >= j+1):
                            a = self.getItems(int(j*math.pow(2,i)), int(j*math.pow(2,i)+2*int(math.pow(2,i-2))) + (1 if i == 1 else 0))
                            b = self.getItems(int(j*math.pow(2,i)+2*int(math.pow(2,i-2))) + (1 if i == 1 else 0), int(j*math.pow(2,i)+4*int(math.pow(2,i-2))) + (1 if i == 1 else 0))
                            merged = merge(a, b)
                            for r in range(len(merged)):
                                self[int(j*math.pow(2,i))+r].data = merged[r].data
                            print(self)
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

    def getData(self):
        current = self.head
        info = "["
        while(current):
            if type(current.data) == List:
                info += current.data.data.getData() + ","
            else:
                info += str(current.data.data) + ","
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
class Elem:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

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
    
    def __getitem__(self, index):
        e = self.head
        while not self.index(e) == index:
            e = e.next
            if e == None:
                print("Index out of range")
                break
        return e
    
    def sort(self):
        for i in range(len(self)):
            for j in range(i+1,len(self)):
                if self[i].data > self[j].data:
                    self[i].data, self[j].data = self[j].data, self[i].data
        print(self)
        
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
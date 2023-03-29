class ArrayList():
    def __init__(self):
        self.arr = [None] * 1
        self.size = 1

    def append(self, data):
        def append_wrapper():
            for i in range(0, self.size):
                l = len(self)
                if self.arr[i] == None:
                    self.arr[i] = data
                    return True
            return False
        
        res = append_wrapper()
        if res == False:
            self.arr = self.arr + ([None]*self.size)
            self.size *= 2
            self.append(data)
        return
    
    def removeIndex(self, index):
        def remove_wrapper():
            self.arr[index] = None
            if len(self) <= self.size/2:
                return False
            return True
        res = remove_wrapper()
        if res == False:
            self.arr = list(filter(lambda x: x != None, self.arr))
            self.size /= 2
            
    def remove(self, data):
        def remove_wrapper():
            for i in range(len(self)-1):
                if self.arr[i] == data:
                    self.removeIndex(i)
            if len(self) <= self.size/2:
                return False
            return True
        res = remove_wrapper()
        if res == False:
            self.arr = list(filter(lambda x: x != None, self.arr))
            self.size /= 2
                
    def __len__(self):
        l = 0
        for i in self.arr:
            if i == None:
                pass
            else:
                l += 1
        return l

    def __str__(self):
        info = "["
        for i in self.arr:
            if i != None:
                info += (str(i) + ",")
        info = (info[:-1] if len(info) > 1 else info) + "]"

        return info

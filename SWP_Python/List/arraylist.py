class ArrayList():
    def __init__(self):
        self.arr = []
        self.size = 10

    def append(self, data):
        def append_wrapper():
            if len(self.arr) < self.size:
                self.arr.append(data)
                return True
            else: return False
        res = append_wrapper()
        if res == False:
            self.size *= 2
            self.append(data)
        return
    
    def removeIndex(self, index):
        def remove_wrapper():
            self.arr.remove(index)
            if len(self) <= self.size/2:
                return False
            return True
        res = remove_wrapper()
        if res == False:
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
            self.size /= 2
                
    def __len__(self):
        l = 0
        for i in self.arr:
            l += 1
        return l

    def __str__(self):
        info = "["
        for i in self.arr:
            info += (str(i) + ",")
        info = (info[:-1] if len(info) > 1 else info) + "]"

        return info
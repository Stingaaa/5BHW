class ArrayList():
    def __init__(self):
        self.arr = [None] * 1
        self.size = 1

    def append(self, data):
        def append_wrapper():
            if len(self) == 0:
                self.arr[0] = data
                return
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
    
    def __len__(self):
        l = 0
        for i in self.arr:
            if i == None:
                break
            else:
                l += 1
        return l

    def __str__(self):
        info = "["
        for i in self.arr:
            if i != None:
                info += (str(i) + ",")
        info = info[:-1] if len(info) > 1 else info + "]"

        return info

arraylist = ArrayList()

for i in range(50):
    arraylist.append(i)

print(len(arraylist))
print(arraylist)
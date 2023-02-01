import random
import time
import mylist

if __name__ == "__main__":
    start = time.time()
    l = mylist.List()
    for i in range(1000):
        l.add(random.randint(0,1000))
    print(l)
    print("\nItems from 2-7:")
    print(l[2:8])
    print("\nSplit List:")
    splitList = l.split(29)
    print(splitList)
    print("\nSorted:")
    print(splitList.sort("merge"))  #or .sortMerge() => own logic
    print("\nShuffled:")
    print(l.shuffle())
    for i in range(990):
        l.removeIndex(0)
    print("\nRemoved\n",l,"\n\nInserted:")
    splitList[0].insert(5,123)
    print(splitList[0])
    end = time.time()
    print((end-start)*1000)
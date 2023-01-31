import random
import mylist

if __name__ == "__main__":
    l = mylist.List()
    for i in range(100):
        l.add(random.randint(0,1000))
    print(l)
    print("\nItems from 2-7:")
    print(l[2:8])
    print("\nSorted:")
    print(l.sort("merge"))
    print("\nSplit List:")
    splitList = l.split(9)
    print(splitList)
    print("\nShuffled:")
    print(l.shuffle())
    for i in range(90):
        l.removeIndex(0)
    print("\nRemoved\n",l,"\n\nInserted:")
    splitList[0].insert(5,123)
    print(splitList[0])
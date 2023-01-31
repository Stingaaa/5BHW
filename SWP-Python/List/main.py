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
        l.remove(l[0])
    print("\n",l)
import random
import mylist

if __name__ == "__main__":
    l = mylist.List()
    for i in range(10):
        l.add(random.randint(0,100))
    l.print()
    print("Sorted:")
    l.sort()
    splitList = l.split(7)
    splitList.print()
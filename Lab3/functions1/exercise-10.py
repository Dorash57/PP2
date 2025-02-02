def uniq(mylist):
    newlist = []
    for x in mylist:
        if mylist.count(x) == 1:
            newlist.append(x)
    return newlist

mylist = list(map(int, input("List: ").split()))
print("New list:", uniq(mylist))

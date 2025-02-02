def histogram(mylist):
    for x in mylist:
        print('*'*x)

mylist=list(map(int, input("List:").split()))
histogram(mylist)
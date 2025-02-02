def reverse_str(mystring):
    mylist=list(mystring.split())
    mylist.reverse()
    for i in mylist:
        print(i,end=" ")

my_str=str(input("String:"))
reverse_str(my_str)

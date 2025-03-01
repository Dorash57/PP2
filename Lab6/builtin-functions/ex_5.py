my_tuple = tuple(map(int, input("Enter elements of tuple: ").split()))
if all(my_tuple):
    print("Yes all elements are true")
else:
    print("Not all elements are true")

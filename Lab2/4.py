#Topics: SETS


                        #PYTHON SETS

#Which one of these is a set?
#myset = {'apple', 'banana', 'cherry'}


#A set cannot have two items with the same value.
#True

thisset = {"apple", "banana", "cherry"}
print(thisset)
#{'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#Here "true" and "1" the same so they considered like duplicate of each other
#{True, 2, 'banana', 'cherry', 'apple'}


thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#{False, True, 'cherry', 'apple', 'banana'}

myset = {'apple', 'banana', 'cherry'}
print(len(myset))
#3


thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.
#{'cherry', 'apple', 'banana'}



                    #ACCESS SET ITEMS

#True or False. You can access set items by referring to the index.
#False



fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#"Yes, apple is a fruit!"


thisset = {'apple', 'banana', 'cherry'}
print('banana' not in thisset)
#False


                        #ADD SET ITEMS

#What is a correct syntax for adding items to a set?
#add()

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
#"apple", "banana", "cherry", "orange"


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
#"apple", "banana", "cherry", "orange", "mango", "grapes"

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}


                    #REMOVE SET ITEMS

#What is a correct syntax for removing an item from a set?
#remove()

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
#apple, cherry

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
#apple, cherry

#Difference: If the item to remove does not exist, discard() will NOT raise an error.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Remove random element
# banana
# {'apple', 'cherry'}


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#set()


thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
##this will raise an error because the set no longer exists

                            #JOIN SETS
#UNION
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#{'c', 2, 3, 1, 'a', 'b'}
#-------------------------
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)
#{'apple', 1, 2, 3, 'cherry', 'John', 'a', 'bananas', 'c', 'Elena', 'b'}
#-------------------------
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
#{'c', 1, 2, 3, 'a', 'b'}
#-------------------------
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
#{1, 2, 3, 'a', 'c', 'b'}


#INTERSECTION
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
#{'apple'}
#-------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)
#{'apple'}
#-------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
#{'apple'}


#DIFFERENCE
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
#{'banana', 'cherry'}
#-------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)
#{'banana', 'cherry'}
#-------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
#{'banana', 'cherry'}

#SYMMETRIC DIFFERENCES
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
#{'google', 'banana', 'microsoft', 'cherry'}
#-------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)
#{'google', 'banana', 'microsoft', 'cherry'}
#-------------------------
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
#{'google', 'banana', 'microsoft', 'cherry'}


#What is a correct syntax for joining set1 and set2 into set3?
#set3 = set1.union(set2)

#What is a correct syntax for joining multiple sets into one new set called set5?
#set5 = set1 | set2 | set3 | set4


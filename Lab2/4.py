#Topics: SETS


                        #PYTHON SETS

#Which one of these is a set?
#myset = {'apple', 'banana', 'cherry'}


#A set cannot have two items with the same value.
#True

myset = {'apple', 'banana', 'cherry'}
print(len(myset))
#3


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

                            #JOIN SETS

#What is a correct syntax for joining set1 and set2 into set3?
#set3 = set1.union(set2)

#What is a correct syntax for joining multiple sets into one new set called set5?
#set5 = set1 | set2 | set3 | set4


#Topics: List

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#<class 'list'>

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#"apple", "banana", "cherry"

mylist = ['apple', 'banana', 'cherry']
print(mylist[1])
#banana

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])
#banana

#List items cannot be removed after the list has been created.
#False

thislist = ['apple', 'banana', 'cherry']
print(len(thislist))
#3

mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])
#Cherry

fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#Banana

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])
#['banana', 'cherry', 'orange']

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#"cherry", "orange", "kiwi"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#['orange', 'kiwi', 'melon']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#['apple', 'watermelon']

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])
#banana

fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])
#mango


mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])
#apple

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
# second element is apple

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)
#apple, lemon, banana, cherry

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)
print(fruits)
#'apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya'


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 
#['apple', 'banana', 'cherry', 'kiwi', 'orange']




                        #REMOVE LIST ITEMS

#What is a List method for removing list items?
#pop()

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
#"apple", "cherry"

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#only first element
#['apple', 'cherry', 'banana', 'kiwi'] 

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)
#['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#Remove the last item:
#['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)
#this will cause an error because you have succsesfully deleted "thislist".

#Select the correct function to remove all items from a list:
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
#clear()

                        #LOOP LISTS
#What is a correct syntax for looping through the items of a list?
for x in ['apple', 'banana', 'cherry']:
  print(x)
#['apple', 'banana', 'cherry']
#------------------------------------
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#  apple
#  banana
#  cherry
#------------------------------------
mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1
#['apple', 'banana', 'cherry']
#------------------------------------
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#  apple
#  banana
#  cherry

#What is a correct syntax for looping through the items of a list?
[print(x) for x in ['apple', 'banana', 'cherry']]


                #LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
#

print(newlist)
#['apple', 'banana', 'mango']

#--------------------------------
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
#['banana']

#--------------------------------
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
#['apple', 'apple', 'apple']

#--------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#['banana', 'cherry', 'kiwi', 'mango']

#--------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
#['apple', 'banana', 'cherry', 'kiwi', 'mango']

#--------------------------------
newlist = [x for x in range(10) if x < 5]
print(newlist)
#[0, 1, 2, 3, 4]

#--------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
#['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

#--------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


                #SORT LISTS

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#--------------------------------
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)
#[50, 65, 23, 82, 100]

#--------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#23, 50, 65, 82, 100

#--------------------------------
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#--------------------------------
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#[100, 82, 65, 50, 23]

#--------------------------------
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#[50, 65, 23, 82, 100]

#--------------------------------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#['Kiwi', 'Orange', 'banana', 'cherry']

#--------------------------------
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#['cherry', 'Kiwi', 'Orange', 'banana']


#What is a correct syntax for sorting a list?
#mylist.sort()

#What is a correct syntax for reversing the current order of a list?
#mylist.reverse()

#What is a correct syntax for sorting a list descending?
#mylist.sort(reverse = True)


                #COPY LISTS
"""
You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2.
"""
#--------------------------------
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#['apple', 'banana', 'cherry']

#--------------------------------
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#['apple', 'banana', 'cherry']

#--------------------------------
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
#['apple', 'banana', 'cherry']

#What is a correct syntax for making a copy of a list?
#1--------list2 = list1.copy()
#2--------list2 = list(list1)
#3--------list2 = list1[:]


                #JOIN LISTS
#What is a correct syntax for joining list1 and list2 into list3?
#1--------list3 = list1 + list2
#2--------list1.extend(list2)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#['a', 'b', 'c', 1, 2, 3]

#--------------------------------
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#'a', 'b', 'c', 1, 2, 3

#--------------------------------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#['a', 'b', 'c', 1, 2, 3]



#Topics: List


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




                        #REMOVE LIST ITEMS

#What is a List method for removing list items?
#pop()

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
#"apple", "cherry"

mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)
print(mylist)
#['apple', 'cherry']

#Select the correct function to remove all items from a list:
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
#clear()

                        #LOOP LISTS
#What is a correct syntax for looping through the items of a list?
for x in ['apple', 'banana', 'cherry']:
  print(x)
#['apple', 'banana', 'cherry']


mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1
#['apple', 'banana', 'cherry']


#What is a correct syntax for looping through the items of a list?
[print(x) for x in ['apple', 'banana', 'cherry']]

                #LIST COMPREHENSION

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
#['banana']

fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
#['apple', 'apple', 'apple']

                #SORT LISTS
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)
#[50, 65, 23, 82, 100]

#What is a correct syntax for sorting a list?
#mylist.sort()

#What is a correct syntax for reversing the current order of a list?
#mylist.reverse()

#What is a correct syntax for sorting a list descending?
#mylist.sort(reverse = True)


                #COPY LISTS
#What is a correct syntax for making a copy of a list?
#1--------list2 = list1.copy()
#2--------list2 = list(list1)
#3--------list2 = list1[:]


                #JOIN LISTS
#What is a correct syntax for joining list1 and list2 into list3?
#1--------list3 = list1 + list2
#2--------list1.extend(list2)



list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#'a', 'b' , 'c',1, 2, 3



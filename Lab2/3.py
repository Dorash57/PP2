#Topics: TUPLES


                    #Python Tuples
#Which one of these is a tuple?
#thistuple = ('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')

#--------------------------------
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#"apple", "banana", "cherry", "apple", "cherry"

#--------------------------------
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#3

#--------------------------------
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#<class 'tuple'>
#<class 'str'>

#--------------------------------
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#"apple", "banana", "cherry"
#--------------------------------
thistuple = ("apple",)
print(type(thistuple))
#--------------------------------
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple items cannot be removed after the tuple has been created.
#True


                    #ACCESS TUPLES
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#apple

fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#('cherry', 'orange', 'kiwi', 'melon', 'mango')

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
#"cherry", "orange", "kiwi"

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#"orange", "kiwi", "melon"


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#Yes, 'apple' is in the fruits tuple

                    #UPDATE TUPLES

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#(apple", "kiwi", "cherry")


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#("apple", "banana", "cherry", "orange")


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#("apple", "banana", "cherry", "orange")


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
#('banana', 'cherry')



                    #UNPACK TUPLES
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
#banana

fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
#['banana', 'cherry']

fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
#['banana', 'cherry']

                    #LOOP TUPLES

for x in ('apple', 'banana', 'cherry'):
  print(x)
#'apple', 'banana', 'cherry'


mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < (mytuple):
  print(mytuple[i])
  i = i + 1
#'apple', 'banana', 'cherry'


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#"apple", "banana", "cherry"

                    #JOIN TUPLES

tuple1 = (1,2,3)
tuple1 = tuple1 * 2
print(tuple1)
#1,2,3,1,2,3

tuple1 = ('a', 'b' , 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1
print(tuple3)
#(1, 2, 3, 'a', 'b', 'c')




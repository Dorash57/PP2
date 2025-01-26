#Topics: TUPLES


                    #Python Tuples
#Which one of these is a tuple?
#thistuple = ('apple', 'banana', 'cherry')

fruits = ("apple", "banana", "cherry")
print(len(fruits))
#3

#Tuple items cannot be removed after the tuple has been created.
#True

                    #ACCESS TUPLES
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#apple

fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#cherry

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
#"cherry", "orange", "kiwi"

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
for i in ((thistuple)):
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




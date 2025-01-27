#Topic: Variables-Global variable

x=5
print(x)
#Output: 5

x="string"
print(type(x))
#Output: <class 'str'>


carname="Volvo"
print(carname)
#Output: Volvo


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
#Sally



x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


x=50
print(x)
#Output:50


x = y = z = 'Hello World'
print(x,y,z)
#Output: Hello World Hello World Hello World

x,y,z = "Orange", "Banana", "Cherry"
print(x,y,z)
#Output: Orange Banana Cherry

fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)
#Correct answer for a it's apple


print("Hello","World")
#Hello World


a = 'Hello'
b = 'World'
print(a + b)
#HelloWorld


a = 4
b = 5
print(a + b)
#9


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#Python is awesome


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Python is awesome

x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
#Python is awesome


def myfunc():
  global x
  x = "fantastic"


x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
#Python is fantastic


#Topics: Booleans-Operators

                          #Booleans:

print(5 > 3)
#True

print(10 > 9)
#True

print(10 == 9)
#False

print(10 < 9)
#False

print(bool("abc"))
#True

print(bool(0))
#False


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#b is not greater than a


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# True
# True
# True


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
# False
# False
# False
# False
# False
# False
# False


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#False

#----------------------------

def myFunction() :
  return True

print(myFunction())
#True

#----------------------------
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
#YES!

#----------------------------
x = 200
print(isinstance(x, int))
#True




                              #Operators:

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))
#0


x = 5
x += 3
print(x)
#5+3=8

print(10*5)
#50

print(10/2)
#5

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#Yes, apple is a fruit!

if 5!=10:
  print("5 and 10 is not equal")
#5 and 10 is not equal

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")


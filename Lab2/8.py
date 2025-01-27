#Topics: For Loops


for x in range(3):
  print(x)
#0
#1
#2

for x in "banana":
  print(x) 
# b
# a
# n
# a
# n
# a


fruits = ["apple", "banana", "cherry"]
for x  in fruits:
  print(x)
#apple
#cherry
#banana


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#apple
#cherry



for x in range(6):
  print(x)
# 0
# 1
# 2
# 3
# 4
# 5


for x in range(2, 6):
  print(x)
# 2
# 3
# 4
# 5


for x in range(2, 30, 3):
  print(x)
# 2
# 5
# 8
# 11
# 14
# 17
# 20
# 23
# 26
# 29



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#apple
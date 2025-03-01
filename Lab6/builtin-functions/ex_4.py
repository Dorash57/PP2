import time
from math import sqrt

num=int(input("Enter a number: "))
res=sqrt(num)

milliseconds=int(input("Enter delay in milliseconds:"))
seconds=milliseconds/1000

time.sleep(seconds)

print(res)
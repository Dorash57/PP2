from functools import reduce
from operator import mul


numbers =list(map(int, input("Numbers: ").split()))
result = reduce(mul, numbers)

print("Result: ", result)

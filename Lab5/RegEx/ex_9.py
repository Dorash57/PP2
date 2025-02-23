import re


txt = input("Enter a string: ")
result=re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
print(result)

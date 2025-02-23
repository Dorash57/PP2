import re

txt=input("Text: ")
result=re.findall(r"[A-Z]?[a-z]+", txt)
my_str=" ".join(result)
print(my_str)

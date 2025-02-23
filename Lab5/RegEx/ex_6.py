import re 

txt=input("Text: ")
pattern=r"[\s,.]"
result=re.sub(r"[\s,.]", ":", txt)
print(result)
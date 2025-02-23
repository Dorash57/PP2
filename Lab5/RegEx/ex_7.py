import re

txt=input("Snake case string: ")
result=re.split('_', txt)

my_str=result[0].lower()+ "".join(word.title() for word in result[1:])
 
print(my_str)

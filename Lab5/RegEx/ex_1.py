import re


text=input("Text: ")
if re.fullmatch(r'ab*$', text):
    print("Yes")
else:
    print("No")
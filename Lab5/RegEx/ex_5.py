import re

txt=input("Text: ")

pattern=r"^a.*b$"

if re.fullmatch(pattern, txt):
    print("Yes")
else:
    print("No")
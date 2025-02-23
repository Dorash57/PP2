import re

txt=input("Text: ")

if re.fullmatch(r"^ab{2,3}$", txt):
    print("Yes")
else:
    print("No")
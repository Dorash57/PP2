import re

txt=input("Text: ")
pattern=r"^[A-Z][a-z]*$"

if re.search(pattern, txt):
    print("YES")
else:
    print("NO")

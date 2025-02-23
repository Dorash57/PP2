import re

txt = input("Text: ")
pattern = r"^(?=.*[a-z])^[a-z_]*_[a-z_]*$"
if re.fullmatch(pattern, txt):
    print("Yes")
else:
    print("No")

import string
import os

folder_name='letters'

for name in string.ascii_uppercase:
    filename=os.path.join(folder_name, f"{name}.txt")
    with open(filename, 'w') as file :
        file.write("KBTU")

print("Files created")
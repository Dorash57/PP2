import os

path=input("Please enter the path: ")

if os.path.exists(path):
    if os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
        print("The file removed successfully")
    else:
        print("You don't have permission to remove this file")
else:
    print("The file doesn't exist")
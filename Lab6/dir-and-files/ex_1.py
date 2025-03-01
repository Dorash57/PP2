import os

path=input("Enter the path:")

print("\n Directories: ")
for item in os.listdir(path):
    full_path=os.path.join(path, item)
    if os.path.isdir(full_path):
        print(item)

print("\n Files and Directories: ")
for item in os.listdir(path):
    print(item)


print("\n Files in specified path: ")
path1=input("Please enter the path: ")
for item in os.listdir(path1):
    full_path1=os.path.join(path1, item)
    if os.path.isfile(full_path1):
        print(item)

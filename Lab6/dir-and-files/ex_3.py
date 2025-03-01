import os

path=input("Please enter the path: ")

if os.path.exists(path):
    if os.path.isdir(path):
        print(f"Directory: \n{path}")
        print("\nItems:")
        for item in os.listdir(path):
            print(item)
    else:
        print(f"The path exists, but it is not a directory: {path}")
else:
    print("The path doesn't exist")
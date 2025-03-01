my_list=list(input("Enter elements of list:").split())

with open("test_1.txt", "a") as file:
    for item in my_list:
        file.write(item+"\n")


with open("test_1.txt", "r") as file:
    content=file.read()
    print(content)
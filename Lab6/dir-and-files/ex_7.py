

with open("test_1.txt", "r") as file:
    content=file.read()


with open("test_2.txt", 'a') as file:
    file.write(content)

with open("test_2.txt", 'r') as file:
    content=file.read()
    print(content)
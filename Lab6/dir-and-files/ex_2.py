import os

path=input("Please enter the path: ")

                #Проверка на существование
if os.path.exists(path):
    print("Yes, this path exists")
else:
    print("No, this path doesn't exist")

                #Проверка на читаемость
if os.access(path, os.R_OK):
    print("Yes this path readable")
else:
    print("No this path isn't readable")

                #Проверка на запись
if os.access(path, os.W_OK):
    print("Yes this path writeable")
else:
    print("No this path isn't writeable")

                #Проверка на выполнение действий
if os.access(path, os.X_OK):
    print("Yes, this path executable")
else:
    print("No this path isn't executable")
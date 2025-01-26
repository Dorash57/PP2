#Topics: Dictionaries



                                #PYTHON DICTIONARIES

#Which one of these is a dictionary?
#x = {'type' : 'fruit', 'name' : 'banana'}

#Dictionary items cannot be removed after the dictionary has been created.
#False

#A dictionary cannot have two keys with the same name.
#True


x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))

                            #ACCESS ITEMS

#True or False. You can access item values by referring to the key name.
#True

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#Mustang


x = {'type' : 'fruit', 'name' : 'banana'}
print(x['type'])
#fruit

                        #CHANGE ITEMS

x = {'type' : 'fruit', 'name' : 'banana'}
#What is a correct syntax for changing the type from fruit to berry?
#x['type'] = 'berry'


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]="2020"
print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': '2020'}

x = {'type' : 'fruit', 'name' : 'banana'}
#What is a correct syntax for changing the name from banana to apple?
#x.update({'name': 'apple'})


                        #ADD ITEMS

#Which one of these dictionary methods can be used to add items to a dictionary?
#update()

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

print(car)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color':'green'})
print(x)
#{'type': 'fruit', 'name': 'apple', 'color': 'green'}


                    #REMOVE ITEMS

#What is a dictionary method for removing an item from a dictionary?
#pop()

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
#{'brand': 'Ford', 'year': 1964}


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
#{}

myvar = {'type' : 'fruit', 'name' : 'apple', 'color' : 'red'}
del myvar['color']
print(myvar)
#{'type': 'fruit', 'name': 'apple'}


                            #NESTED DICTIONARIES 

a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
#what will be a correct syntax for printing the name 'May'?
#print(customers['c2']['name']

a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
  print(x)
    
  for y in obj:
    print(y + ':', obj[y])



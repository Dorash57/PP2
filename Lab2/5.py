#Topics: Dictionaries



                                #PYTHON DICTIONARIES

#Which one of these is a dictionary?
#x = {'type' : 'fruit', 'name' : 'banana'}

#Dictionary items cannot be removed after the dictionary has been created.
#False

#A dictionary cannot have two keys with the same name.
#True

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#-------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#Ford

#-------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#-------------------------
x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))
#2
#-------------------------
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#{'name': 'John', 'age': 36, 'country': 'Norway'}


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

#-------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#dict_keys(['brand', 'model', 'year'])
#dict_keys(['brand', 'model', 'year', 'color'])

#-------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
#dict_keys(['brand', 'model', 'year'])

#-------------------------
x = {'type' : 'fruit', 'name' : 'banana'}
print(x['type'])
#fruit

#-------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
#dict_values(['Ford', 'Mustang', 1964])
#dict_values(['Ford', 'Mustang', 2020])

#-------------------------
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

#-------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
#Yes, 'model' is one of the keys in the thisdict dictionary



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

#-------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#-------------------------
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

#-------------------------
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


#-------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang'}


#-------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#{'brand': 'Ford', 'year': 1964}


#-------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#-------------------------
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


                            #LOOP DICTIONARIES
#VALUES
#1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
# brand
# model
# year

#2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
#-------------------------
#KEYS
#1
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
# Ford
# Mustang
# 1964

#2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
# brand
# model
# year
#-------------------------


                            #COPY DICTIONARIES

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


                            #NESTED DICTIONARIES 

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 
# 'child2': {'name': 'Tobias', 'year': 2007}, 
# 'child3': {'name': 'Linus', 'year': 2011}}




child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
#{'child1': {'name': 'Emil', 'year': 2004}, 
#'child2': {'name': 'Tobias', 'year': 2007}, 
#'child3': {'name': 'Linus', 'year': 2011}}



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])
#Tobias




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
# c1
# name: John
# age: 20
# c2
# name: May
# age: 23


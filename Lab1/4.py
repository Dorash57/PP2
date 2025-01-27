#Topic: String-Format Strings

x = 'Welcome'
print(x[3])
#с

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
# It's alright
# He is called 'Johnny'
# He is called "Johnny"


a = "Hello"
print(a)
#Hello


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.


x = "Hello World"
print(len(x))
#11


txt = "Hello World"
x = txt[0]
print(x)
#H


txt = 'The best things in life are free!'
if 'free' in txt:
  print('Yes, free is present in the text.')
#Yes, free is present in the text.

txt = "The best things in life are free!"
print("expensive" not in txt)
#True

x = 'Welcome'
print(x[3:5])
#co


b = "Hello, World!"
print(b[-5:-2])
#orl


txt = "Hello World"
x = txt[2:5]
print(x)
#llo


x = 'Welcome'
print(x[3:])
#come


txt = " Hello World "
x = txt.strip()
print(x)
#Hello World


txt = "Hello World"
txt = txt.upper()
print(txt)
#HELLO WORLD


txt = "Hello World"
txt = txt.lower()
print(txt)
#hello world


txt = "Hello World"
txt = txt.replace("H", "J")
print(txt)
#Jello World


a = "Hello, World!"
b = a.split(",")
print(b)
#['Hello', ' World!']


x = 'Welcome'
y = 'Coders'
print(x + y)
#WelcomeCoders

a = 'Join'
b = 'the'
c = 'party'
print(a + ' ' + b + ' ' + c)
#Join the party


x=9
print(f'The price is {x:.2f} dollars')
#The price is 9.00 dollars


age = 36
txt = f"My name is John, and I am {age}"
print(txt)
#My name is John, and I am 36


print(f'The price is {2 + 3} dollars')
#The price is 5 dollars


txt = "We are the so-called \"Vikings\" from the north."
#We are the so-called "Vikings" from the north.
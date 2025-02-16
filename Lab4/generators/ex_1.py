def my_function(num):
    for x in range(num):
        x+=1
        yield x*x

number=int(input())
a=my_function(number)
print(type(a))
for x in a:
    print(x)

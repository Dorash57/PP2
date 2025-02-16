def countdown(n):
    x=n
    while x>=0:
        yield x
        x-=1

n=int(input("Enter N: "))
rev=countdown(n)
print(', '.join(str(x) for x in rev))

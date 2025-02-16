def squares_from_a_to_b(a, b):
    for x in range(a, b+1):
        yield x**2

a=int(input("A:"))
b=int(input("B:"))
square=squares_from_a_to_b(a, b)
print(', '.join(str(x) for x in square))
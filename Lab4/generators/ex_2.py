def generator_even_numbers(num):
    for x in range(num+1):
        if x%2==0:
            yield x

san=int(input("san: "))
g=generator_even_numbers(san)
print(', '.join(str(x) for x in g ))
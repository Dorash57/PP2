# def permutations(mystr):
#     n=len(mystr)
#     for i in range(n):
#         for j in range(n):
#             print(mystr[(j-i)], end=" ")


# mystr=str(input("String: "))
# permutations(mystr)


def permutations(some):
    n = len(some)

    for i in range(n):
        for j in range(n):
            print(some[(j-i)], end=" ")
        print()
k=str(input("soz:"))
permutations(k)
def div_3_4(value):
    for x in range(value+1):
        if x%3==0 and x%4==0:
            yield x


num=int(input("num: "))
d=div_3_4(num)
print(', '.join(str(x) for x in d))
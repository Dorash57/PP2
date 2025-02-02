def prime(num):
    if num<2:
        return False
    if num==2 or num==3:
            return True
    for i in range(2, int(num**(0.5)+1)):
        if num%i==0:
            return False
    return True

def filter_prime(mylist):
    prime_numbers=[x for x in mylist if prime(x)]
    return prime_numbers


mylist=list(map(int, input("Numbers: ").split()))
print("Prime numbers:",filter_prime(mylist))
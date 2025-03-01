

myString=input("Text: ")
upper_letter=0
lower_letter=0
for x in myString:
    if x.isupper():
        upper_letter+=1
    elif x.islower():
        lower_letter+=1

print("Upper case letters:", upper_letter)
print("Lower case letter:", lower_letter)

myString=input("String: ")
reversed_String=myString[::-1]
print(myString, reversed_String)
if myString==reversed_String:
    print("Yes this string is palindrome")
else:
    print("No this string is not palindrome")
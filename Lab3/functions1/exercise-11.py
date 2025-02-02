def palindrom(word):
    word=word.lower()
    if word==word[::-1]:
        print("YES")
    else:
        print("NO")

word = input("word: ")
palindrom(word)
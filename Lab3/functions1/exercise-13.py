import random
def guess_the_number(name):
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    random_number=random.randint(1, 20)
    count=0
    while True:
        print("\nTake a guess.")
        count+=1
        num=int(input())
        
        if random_number>num:
            print("Your guess is too low.")
        elif random_number<num:
            print("Your guess is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {count} guesses!")
            break



print("Hello! What is your name?")
name=input()
guess_the_number(name)


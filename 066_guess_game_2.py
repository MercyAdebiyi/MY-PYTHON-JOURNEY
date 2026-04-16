import random


my_number=random.randint(1,100)
guess_number=int(input("Guess my number: "))
guess_count=1


while guess_number!=my_number:
    print("wrong number")
    
    if guess_number>my_number:
        print("number too high. Guess lower")
    elif guess_number<my_number:
        print("number too low. Guess higher")

    guess_number=int(input("Guess my number: "))
    guess_count+=1

else:
    print(f"Hurray!! You guessed right. The number is {my_number}. It took you {guess_count} guesses.")

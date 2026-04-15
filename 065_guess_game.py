# Set a secret number (e.g. `7`).
# Keep asking the user to guess the number until they get it right.

# Tell the user if their guess is **too high** or **too low**

my_number=10
guess_number=int(input("Guess my number: "))

while guess_number!=my_number:
    print("wrong number")
    
    if guess_number>my_number:
        print("number too high. Guess lower")
    elif guess_number<my_number:
        print("number too low. Guess higher")

    guess_number=int(input("Guess my number: "))

else:
    print("Hurray!! You guessed right")

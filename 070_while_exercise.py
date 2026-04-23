age=int(input("enter your age: "))

while age>=18:
    if age>25:
        print("you are old")
        choice=input("enter yes/no to play again")
        if choice=="yes":
            continue
        else:
            break
    else:
        print("you are a young adult")
        choice=input("enter yes/no to play again")
        if choice=="yes":
            continue
        else:
            break
else:
    print("You are a child")

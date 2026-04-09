# age=int(input("Ente your age"))

# while age<18:
#     print(f"you are {age} years old child")
#     age=age +1
# else:
#     print("you are an adult")




# age=int(input("Ente your age"))

# while age<18:
#     print(f"you are {age} years old child")
#     if age==15:
#         break
#     age=age +1
# else:
#     print("you are an adult")

# age=int(input("Ente your age"))

# while age<18:
#     print(f"you are {age} years old child")
#     age=age +1
#     if age==15:
#         continue
    
# else:
#     print("you are an adult")



choice=input("enter yes or no to play: ").strip().lower()

while choice=="yes":
    age=int(input("enter a NUMBER TO guess my age: "))
    if age <28:
        print("guess higher")
    elif age>28:
        print("guess lower")
    else:
        print("you guessed right.")
        choice=input("enter yes or no to play: ").strip().lower()

else:
    print("Goodbye")
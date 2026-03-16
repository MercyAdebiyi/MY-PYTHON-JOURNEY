age=int(input("enter your age: "))

if age >=17:
    provisional_licence=input("Do you have a provisional licence 'yes' or no").strip().lower
    if provisional_licence=="yes":
        print("You can learn to drive")
    else:
        print("You need a provisional licence")

else:
    print("\nYou are too \n\nyoung to drive\n")
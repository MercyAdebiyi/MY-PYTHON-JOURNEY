# nested if is used to input multiple conditions in a program

# example is student grade. if a student scores certain score we want to know if they passed and another conditiojn to know if it was a positive or negative score

grade=float(input("Enter your grade: "))

if grade >=70:
    print("Congratulations!! You passed.")
    # 2 conditions that warranted for only if and else 
    if grade>=80:
        print("Your grade is A+")
    else:
        print("Your grade is A-")


elif grade>=60:
    print("Congratulations!! You passed.")
    # 3 conditions that warranted for if, elif, and else 
    if grade==65:
        print("Your grade is B")
    elif grade>65:
        print("Your grade is B+")
    else:
        print("Your grade is B-")

elif grade>=50:
    print("Congratulations!! You passed.")

    if grade>=55:
        print("Your grade is C+")
    else:
        print("Your grade is C-")

elif grade>=40:
    print("Congratulations!! You passed.")

    if grade>=45:
        print("Your grade is D+")
    else:
        print("Your grade is D-")

else:
    print("Sorry!! You failed this course.")
    print("You scored F")
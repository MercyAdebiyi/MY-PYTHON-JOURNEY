

# age=float(input("Enter age: "))

# if age <=10:
#     if age<6:
#         print("You are less than 6 years old")
#     else:
#         print("you sre 6 years and above")

# else:
#     print("adult.")
 


name=input("Enter bible characater (Abrahma, Lot, or Sarah): ").strip().capitalize()

if name=="Abraham":
    print("you selected abraham.")
    journey=input("Where would you go to? (canaan or egypt)").strip().lower()
    if journey=="canaan":
        print("\nyou will be the father of all nations\n")
    else:
        print("\nyou will perish in Gomorra\n")

elif name=="Lot":
    print("you selected Lot.")
    journey=input("where would you go to? (paris or bethel): ").strip().lower()
    if journey=="paris":
        print("\nyou are abrahame'nices\n")
    else:
        print("\nyou will leave abraham'house\n")

elif name=="Sarah":
    print("\you selected Sarah.\n")
    journey=input("where would you go to? (nazareth or Sodum): ")
    if journey=="nazareth":
        print("\nyou are in holy land\n")
    else:
        print("\nthat is the wrong destisnation\n")

else:
    print("invalid response")
# logical operators are "and" and "or" statements. They can be used in place of nested if statements

age =20
name="sam"
food="rice"
meat="turkey"

# if age==20:
#     print("you are a adult")
#     if name=="sam":
#         print("welcome")
# else:
#     print("you are a child")

# if age==20 and name=="sam":
#     print("You are adult. Welcome.")

# else:
#     print("you are a child")

if food=="rice" and meat=="asun":
    print("both choice is available")

elif food=="rice" or meat=="asun":
    print("one choice available")

else:
    print("both food not available")

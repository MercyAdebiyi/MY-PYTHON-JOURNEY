# OPERATORS REVISION

# 1. Assignment operators: =, +=, -=, *=. /=, %=, **=
# 2. Arithemetic operator: +, -, /, *, **, %
# 3. Comparison operatoes: ==, !=, >, <, >=, <=
# 4. Logical opeators: and, or, not
# 5. Membership operator: in





# membership operator is used to check if a value is a member of a giver variable, list or dictionary. The membership operator return a boolean datatype. 

# print("*************Membership Operators****************")


# family="Samson, Mercy, Tijesu"

# family_members= "Mercy" in family 
# print(family_members)


# print("*************EXERCISE 1****************")

# check_name= input("Please enter name to check if you are a member of this village: ").lower().strip()

# villagers= "umar, isah, sadiq, ahmed, bala, fatima, hadiza, rukayat, asmau, sani, semaiya, ibrahim, mohammad, aisha"

# if "a" in villagers:
#     print("You are a member of the vilage.")
# else:
#     print("who be your papa!!!")

# print()

# print("*************EXERCISE 2****************")
# guess=input("guesss the alphabets in my name: ").strip().title()
# name="Mercy"

# print(f"name contain alphabet {guess.upper()}") if guess in name else print(f"ALPHABET {guess.lower()} NOT IN MY NAME")

# print()

print("*************EXERCISE 4****************")

address="vicarage lane"
t_or_f= "z" not in address
print(t_or_f)

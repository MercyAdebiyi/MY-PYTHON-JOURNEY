# TABS AND NEW LINES 


# option 1
# print("") #new line was inserted manually using an empty print statement
# print("Samson")
# print("Tinub")
# print("Hassan")
# print("Wale")
# print("Aminu")
# print("Moses") 
# print("") #new line was inserted manually using an empty print statement

# age=23
# name="Samson"
# height=1.3

# # option 2: use multiline to print in many lines.

# print(f"""Hi {name}
# You age is {age}
# Your height is {height}

# """)

# option 3: use the back slash to create new line (\n)

# print(f"\nour age= {age} \nYour name= {name} \nYour height={height}\n")


# TAB 
# tab is an indent that can be added using the backslash and t (\t)

# print("\tJesus is Lord")


# NUMBER METHOD
# this methods are available to floats and int to carryout maths operation


# 1. round() method helps to round a number up or down, or to specific decimal places
x=12.64744
y=4.2322222
total=x*y
total_rounded=   round(x*y)
decimal_rounded_total=round(total, 3)
print(f"\nThe total is {total} and rounded total is {total_rounded}, and the decimals are {decimal_rounded_total}\n")

# a shorthand to perform the round method is below
z=66.37474839238393
print(f" The number is {z:.4f}")    


# 2. absolute: this converts any negative number to positive 

j= -12.3464646464
j_absolute=abs(j)
print(f"the number turned to positive {j_absolute}")


# a shorthand to perform the absolute method is below:
print(f"the shorthand absolute is {j.__abs__():.2f} 😂😂😂😂") #turns it to absolute and 2 decimal places


# data types: 
# strings, numbers (floats and int)

# string methods:
# .lower(), .upper(), .title(), .strip(), .lstrip(), .rstrip(), .find(), .replace(), .count(), .startswith(), .endswith(), .isalpha(), .isdigit(), .isspace(), .join(), .split(), isalnum(), isalpha, isdecimal(), isdigit(), islower(), isnumeric(), isprintable(), isspace(), istitle(), isupper()

# STRING SLICING
# This is done with indexing and slicing notation using square brackets [ ].

# Example 1:
name= "Samson"
inde= "012345"
inex="-6,-5,-4,-3,-2,-1"

print("**********POSITIVE INDEXING******************")



print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

print("**********NEGATIVE INDEXING******************")

print(name[-6])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])


print("**********REVERSING A STRINF******************")

print(name[::-1])


print("**********PALLINDROME EXERCISE******************")

# word= input("enter a pallindrome word: ")

# if word== word[::-1]:
    # print(f"{word} is a pallindrome")
# else:
    # print(f"{word} is not a pallindrome")

# TENERARY OPERATOR: IT IS USED TO WRITE THE IF ELSE CONDITION IN A SINGLE LINE

# print(f"{word} is a pallindrome") if word== word[::-1] else print(f"{word} is not a pallindrome")

print("**********SLICING STRING BY RANGE******************")

name2= "Mercy"
inxi1= "01234"
print(name2[0:3])
print(name2[0:5])
print(name2[2:4])

print("**********SLICING ALL******************")
greet = "Hello, My name is Mercy. I live in Kenya. I am 23 years old."

name=greet[18:23]
country=greet[35:41]
age=greet[47:]

# multiple variables declaration
name, country, age= greet[18:23], greet[35:41], greet[47:]

print(f"Name: {name}, Country: {country} Age: {age} years old.")
print(name2[:])
print(name2[::])
print(name2[1:])
print(greet[7:])
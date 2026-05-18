# ******************
#    Exercise 1
# ******************
# Create a dictionary called `student` with keys: `name`, `age`, and `course`. Assign appropriate values and print the dictionary.


student= {"name": "John Doe", "age": 25, "courses": ["Math", "CompSci"]}
# 
print(student)
print()


# ******************
#    Exercise 2
# ******************
# Access and print the value of `name` from the `student` dictionary.

# print(student["name"])


# ******************
#    Exercise 3
# ******************
# Add a new key `grade` to the `student` dictionary with a value of `"A"`.

# student['grade']='A'
# print(student)


# ******************
#    Exercise 4
# ******************
# Update the `age` of the student to a new value.

# student["age"]=50
# print(student)


# ******************
#    Exercise 5
# ******************
# Remove the `course` key from the dictionary.

# del(student["courses"])
# print(student)


# ******************
#    Exercise 6
# ******************
# Print all the keys in the dictionary.

# print()
# print(student.keys())


# ******************
#    Exercise 7
# ******************
# Print all the values in the dictionary.
# print()
# print(student.values())


# ******************
#    Exercise 8
# ******************
# Print all key-value pairs using a loop.

# for q, z in student.items():
#     print(z, q)


# ******************
#    Exercise 9
# ******************
# Check if the key `email` exists in the dictionary.

# print()
# if "email" in student:
#     print("email exists")
# else:
#     print("email absent")


# ******************
#    Exercise 10
# ******************
# Create a dictionary of 3 countries and their capitals. Print each country with its capital.

# country={"nigeria":"abuja" , "united kingdom":"london" , "ghana":"accra"}
# for key,value in country.items():
    # print(f"{value} is the capital of {key} \n\n")


# ******************
#    Exercise 11
# ******************
# Create a dictionary `numbers` with values from 1–5. Calculate the sum of all values.

number={"one":1, "two":2, "three":3, "four":4,"five":5 }
total=sum(number.values())
# print(total)


# ******************
#    Exercise 12
# ******************
# Write a program to count how many times each letter appears in a word using a dictionary.
# word={"name": "Samsonsonsam"}
# word["name"] = word.get("name", 0)
# print(word)


# Ask user for input
word = input("Enter a word: ")

# Create an empty dictionary
letter_count = {}

# Loop through each letter in the word
for letter in word:                
    letter_count[letter] = letter_count.get(letter, 0) + 1

# Display the result
print("Letter counts:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")













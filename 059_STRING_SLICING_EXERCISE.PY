print("*****************exercise 1****************")

# Using start, stop, and step**
#   Using the string `word = "programming"`, extract every second character starting from index 0.

word="programming"

print(f"{word[0:11:2]}")


print("*****************exercise 2****************")

#  Negative indexing**
#   Given `name = "NewhamCollege"`, use slicing to get the last 7 characters.

name="NewhamCollege"

print(f"{name[-7:]}")


print("*****************exercise 3****************")

#  Reversing a string**
#   Using slicing only, reverse the string `sentence = "Python is fun"`.

sentence="python is fun"
print(f"{sentence[::-1]}")


print("*****************exercise 3****************")

#  Removing characters with slicing**
#   Given `email = "user@example.com"`, use slicing to remove the domain part (`"@example.com"`) and keep only the username.

email="user@example.com"

print(f"{email[0:4]}")
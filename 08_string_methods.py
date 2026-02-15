name= "Samson's house"

age= 30

# multi-line string. 
# it is used to create strings that span multiple lines. it is done using triple quotes (""" or ''').

print(f"""Hi, i am glad to have everyone here in this meeting. 
My name is {name} and I am {age} years old.
Welcome to my house!""")






# STRING METHODS
# They are built-in functions that perform specific operations on strings. Here are some commonly used string methods with examples:

# method 1: .upper()
name= "mercy adebiyi"
print(name.upper())  # converts all characters to uppercase

# method 2: .lower()
name2= "DAVID OKEKE"
print(name2.lower())  # converts all characters to lowercase

# method 3: .capitalize()
name3= "john smith"
print(name3.capitalize())  # capitalizes the first character of the string


# method 4: .title()
name4="segun johnson adebola taiwo"
print(name4.title())  # capitalizes the first character of each word in the string


# method 5: .strip()
name5="   emma oluwaseun   "
print(name5.strip())  # removes leading and trailing whitespace


# method 6: .replace()
name6="Donald Trump"
print(name6.replace("Trump", "Mercy"))  # replaces occurrences of a substring with another substring. The method is .replace(old, new)


# method 7: .split()
name7="barack obama"
print(name7.split())  # splits the string into a list of substrings based on whitespace


# method 8: .find()
name8="hello world welcome to python programming"
print(name8.find("python"))  # returns the index of the first occurrence of the specified substring. If not found, it returns -1.

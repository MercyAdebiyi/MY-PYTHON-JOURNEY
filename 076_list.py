names=["samson", "mercy", "john", "michael", "susan"]
index=[0, 1, 2, 3, 4]


# 1. List is a collection of items in a particular order. It is one of the most commonly used data structures in Python.

# print(names[2])

# 2. Lists are mutable, which means that you can change their content after they have been created.

# names[0] = "samantha"
# print(names)

# 3. Lists can contain items of different types, including other lists.

life_details= ["samson", 25, "male", 6.23, True]
# print(life_details)

# 4. Lists support various operations such as slicing, concatenation, and repetition.

names_and_life_details = names + life_details
# print()
# print(names_and_life_details)

# 5. List allows duplicates, which means that you can have multiple occurrences of the same item in a list.

# fruits = ["apple", "banana", "orange", "apple", "grape"]
# print()
# print(fruits)

# 6. list can contain other lists as elements, creating a nested list structure.

# nested_list = [1, 2, [3, 4], 5]
# index_nested_list = [0, 1, 2, 3]
# print()
# print(nested_list) 
# 
# print()
# print(nested_list[2]) 
# 
# print()
# print(nested_list[2][0]) 

# 7. finding the length of a list using the len() function.

pets = ["dog", "cat", "hamster", "rabbit"]
# print()
# print(len(pets))
# 
# 8. finding the type of a list using the type() function.
# print(type(pets))

# 9. casting a list to a different data type using the list() function.
string = "1232"
list_from_string = list(string)
print(type(list_from_string))
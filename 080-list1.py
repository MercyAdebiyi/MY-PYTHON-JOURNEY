# 🧠 Exercise 1 — Creating and Accessing Lists

# fruit=["orange", "mango", "apple", "strewberry", "banana"]
# print(fruit[0])
# print(fruit[-1])
# print(fruit[2])
# print(len(fruit))




# 🧠 Exercise 2 — Updating List Elements

# colors = ["red", "blue", "green", "yellow"]

# colors[2]="black"
# print(colors)




# 🧠 Exercise 3 — Adding Items to a List

# colors=[]

# colors.append("red")
# colors.append("green")
# colors.append("blue")

# colors.insert(1, "purple")

# colors.extend(["peach", "grey", "indigo"])
# print(colors)



# 🧠 Exercise 4 — Removing Items from a List

# numbers = [5, 10, 15, 20, 25, 15, 15]
# numbers.remove(15)
# numbers.pop(1)
# numbers.clear()
# print(numbers)


# 🧠 Exercise 5 — Looping Through a List

# numbers=[91, 432, 83, 54, 435, 60]
# for elements in numbers:
#     print(elements)


# 🧠 Exercise 6 — Finding the Sum Manually

# total=0
# age=[2, 28,38]
# for element in age:
#     total=total+element

# print(total)




# 🧠 Exercise 7 — Finding Maximum and Minimum (Without max/min)

# numbers=[21, 82, 32, 741, 17]
# largest_number=0

# for elements in numbers:
#     if elements>largest_number:
#         largest_number=elements
# print(f"the lagest number is {largest_number}")

# lowest_number=100000000

# for elements in numbers:
#     if elements<lowest_number:
#         lowest_number=elements

# print(f"the lowest number is {lowest_number}")




# 🧠 Exercise 8 — List Slicing Practice

# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# print(nums[0:3])
# print(nums[5:8]) 
# print(nums[1:5])
# print(nums[::-1])



#  🧠 Exercise 9 — Counting Specific Elements

# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# even_counter=0
# odd_counter=0

# for elements in numbers:
#     if elements%2==0:
#         even_counter+=1
#     else:
#         odd_counter+=1


# print (f" there  are {even_counter} even numbers and {odd_counter} odd numbers")




# 🧠 Exercise 10 — List Comprehension (Very Important 🔥)

# for elements in range(10):
#     print(elements)

# for elements in range(10, 21):
#     print(elements)

# for elements in range(10, 21, 2):
#     print(elements)

# for i in range(11):
#     print(i**2)

# for j in range(0, 51, 2):
#     print(j)

for k in range(101):
    if k%5==0:
        print(k)
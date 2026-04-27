

# range is used to specify the integers we want to print. Range starts from 0 and the last digit is not printed but acts as a border

# Example 1
# This example prints the values: 0, 1, 2, 3, and 4. The number 5 is the upper boundary

# for element in range(5):
#     print (element)


# example 2
# We can specify the start and end of the range same way as slicing in strings

# for element in range(5, 20):
#     print (element)


# example 3

# one can specify the number of steps to be in the range just like in string slicing

# for element in range(2, 21, 2):
#     print (element)

# example 4:
# A int variable can be used in a range. The range function only accepts intergers

# age=12

# for x in range(age):
#     print (x)


# Example 5:
# Since the range function only accepts intergers, and the length function in python always returns an interger, the len() can be used in range()

# name="Mercy Adebiyi"
name=input("enter anything: ")

for x in range(len(name)):
    print (x)

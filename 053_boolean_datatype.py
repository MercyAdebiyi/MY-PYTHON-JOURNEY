# BOOLEAN DATA TYPE 

# this is a data type that can only be true or false
print("*****************BOOLEAN DATA TYPE*****************")


is_raining= True
print(type(is_raining))  # <class 'bool'>

samson= False
print(type(samson))  # <class 'bool'>

print("*********BOOLEAN IN COMPARISON OPERATORS********")

print(5 > 3)   # True
print(5 < 3)   # False
print(5 == 3)  # False
print(5 != 3)  # True
print(55.5 > 50)  # True

print("*****************BOOLEAN IN CODING*****************")

weight=55.50
if True: #this is the same as if weight>50
    print("You are eligible to donate blood")
else:
    print("You are not eligible to donate blood")   


age1=20
age2=25
age_question=age1 > age2 #FALSE
print(age_question)


if age1 > age2: # or 20>25 or FALSE or age_question
    print("age1 is greater than age2")
else:
    print("age1 is not greater than age2")

print("***********TYPE CONVERSION TO BOOLEAN************")


name= "50"
print(int(name))  # 50
print(float(name))  # 50
print(name)  # 50
print(bool(name))  # True

h= bool(input("enter a number: "))
print(type(h))

#most values convert to TRUE except 0, false, and empty values

bool(False) #false
bool(None) #null value
bool(0) #zero
bool("") #empty string
bool(()) #empty tuple
bool([]) #empty list
bool({}) #empty dictionary

nhfhfh=0
print(bool(nhfhfh))  # False

age=""
if age:  #this is the same as if age
    print("You are eligible to vote")
else:
    print("enter valid age")

print("***********BOOLEANS IN FUNCTIONS************")

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
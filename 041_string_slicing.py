name= "samson"
index="012345"
index_from_back="-6,-5,-4,-3,-2,-1" #this is called negative indexing
print(name)

# string indexing is done with a box bracket and specification of the index to get 
print(f"\n{name[0]}")
print(f"\n{name[1]}")
print(f"\n{name[2]}")
print(f"\n{name[3]}")
print(f"\n{name[4]}")
print(f"\n{name[5]}")

print("----------------NEGATIVE-----------------")

# NEGATIVE INDEXING
print(f"\n{name[-6]}")
print(f"\n{name[-5]}")
print(f"\n{name[-4]}")
print(f"\n{name[-3]}")
print(f"\n{name[-2]}")
print(f"\n{name[-1]}")

print("--------------MULTI SLICE-----------------")

# A colon is used to specify multiple index. the first index number is where to start the slicing from and the last index is where to end. 

#note that multi slicing doesnt print the last end index. it uses it instead as a border.

print(f"\n{name[0:3]}") #positive slicing
print(f"\n{name[-6:-3]}") #negative slicing
print(f"\n{name[0:-3]}") #mixed slicing



print("---------SLICING BY STEPS-----------------")

# an additional instruction to give the steps is used by adding additional colon

print(f"\n{name[0:6:2]}") #this gives output by 2 steps (SMO)
print(f"\n{name[0:6:3]}") #this gives output by 2 steps (SMO)


print("--------REVERSING A STRING-----------------")
# this is done with a double colon (::) followed by -1.
print(f"\n{name[::-1]}")




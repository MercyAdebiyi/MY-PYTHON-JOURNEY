# step 1: I created an emoty list. This is where i will append user entry

items=[]

price=[]
question="yes"
# step 2: I asked the users to enter shopping items and price 
while question=="yes":
    goods=input("please enter the name of goods: ").strip().lower()

    price_goods=input("please enter the price of the goods: ").strip().lower()

    # step 3: I appended entries to the list created in step 1

    items.append(goods)
    price.append(price_goods)

    question=input("Buy more? Enter yes or no: ".strip().lower())

# step 4: I printed the list items 
print(f"{items} \n\n")
print(f"{price} \n\n")


# step 5: I checked the data types to ensure that the list is still a list after appending the inputs

print(type(items))
print(type(price))
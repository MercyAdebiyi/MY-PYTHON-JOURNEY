print("welcome to our restaurant. ")
food=input("choose your meal: rice, semo, asaro, or fish: ").lower().strip()


# first level if statement
if food=="rice":
    print("please Choose one: white rice, fried rice or jollof rice")
    rice_choice=input("Enter rice choice: ").strip().lower()

    # second level if statement 
    if rice_choice=="white rice":
        print("Select meat: chicken, turkey, or ponmo")
        meat_choice=input("Enter meat choice: ")
        
    elif rice_choice=="fried rice":
        print("Select meat: chicken, turkey, or ponmo")
        meat_choice=input("Enter meat choice: ")
    else:
        print("Select meat: chicken, turkey, or ponmo")
        meat_choice=input("Enter meat choice: ")

    print(f"You ordered {food}. {rice_choice} and {meat_choice},")

elif food=="semo":
    print("""Great choice. 
          please selelct a soup: egusi, efo riro, okra, banga """)
    soup=input("enter your soup choose").strip().lower()

    if soup=="egusi":
        print("select meat: beef or goat")
        protein_choice=input("enter meat type: ")
        if protein_choice=="beef":
            print(f"your meat choice is {protein_choice}")
        else:
            print(f"your meat choice is {protein_choice}")

    elif soup=="efo riro":
        print("select meat: beaf or goat")
        protein_choice=input("enter meat type: ")
        if protein_choice=="beef":
            print(f"your meat choice is {protein_choice}")
        else:
            print(f"your meat choice is {protein_choice}")

    elif soup== "okra":
        print("select meat: beaf or goat")
        protein_choice=input("enter meat type: ")
        if protein_choice=="beef":
            print(f"your meat choice is {protein_choice}")
        else:
            print(f"your meat choice is {protein_choice}")

    else:
        print("select meat: beaf or goat")
        protein_choice=input("enter meat type: ")
        if protein_choice=="beef":
            print(f"your meat choice is {protein_choice}")
        else:
            print(f"your meat choice is {protein_choice}")

    print(f"Your order is {food} and {soup} soup with {protein_choice}. Your food will be ready soon.")

elif food=="asaro":
    print("Please Choose one: yam, potato, or plantain. ")
    asaro=input("enter your favorite asaro: ").lower().strip()

    if asaro=="yam":
        print("enter your favorite protein: beef, fish, meat ")
        protein=input("please choose your protein: ")

    elif asaro=="potato":
        print("enter your favorite protein: beef, fish, meat ")
        protein=input("please choose your protein: ")

    elif asaro=="plantain":
        print("enter your favorite protein: beef, fish, meat ")
        protein=input("please choose your protein: ")

    else:
        print("We have no such here ")
        protein=input("enter your favorite: ")

    print(f"You have ordered {asaro} and {protein}. Do have a lovely day today. ")

elif food=="fish":
    print("choose your favorite: grill fish, catfish and tilapia ")
    fish=input("select your favorite fish: ")

    if fish=="grill fish":
        print("enter a drink of your choice ")
        drink=input("choose either soft drink or alcohol: ")

    elif fish=="catfish":
        print("enter a drink of your choice ")
        drink=input("choose either soft drink or alcohol: ")

    else:
        print("tilapia")
        drink=input("choose either soft drink or alcohol: ")

else:
    print("Please choose something on the menu. ")
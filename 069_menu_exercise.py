choice=int(input("""Enter a choice below:
1. Say Hello
2. Say Goodbye
3. Exit
             
"""))

while choice !=3:
    if choice==1:
        print("Hello")
    elif choice ==2:
        print("goodbye")
    choice=int(input("""Enter a choice below:
1. Say Hello
2. Say Goodbye
3. Exit
             
"""))

else:
    print("Exit")
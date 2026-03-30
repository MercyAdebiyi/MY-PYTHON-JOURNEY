# EXERCISE 2
# validate email. Must end with .com, must have 1 @, must not have space 

email= input("enter your email: ")

if not email.isspace():
    print("no space")
    if email.endswith(".com"):
        print("email has .com")
        if email.count("@")==1:
            print("Your email is verified.")


else:
    print("wrong email")





# method 2
email= input("enter your email: ")

if not email.isspace() and email.endswith(".com") and email.count("@")==1:
    print("\n\nyour email is verified")
else:
    print("\n\nwrong email")
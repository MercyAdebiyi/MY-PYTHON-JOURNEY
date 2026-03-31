# EXERCISE 4 
password= input("enter a password: ")

if password.isalnum() and not password.isspace() and len(password)>=6:
    print("strong password")
else:
    print("weak password")





# method 2:
password= input("enter password: ")

if password.isalnum():
    print("password is alphanumeric")
    if len(password)>=6:
        print("good password length")
    else:
        print("short password length")
        if not password.isspace():
            print("psassword has no space")
        else:
            print("password has space")

    print("valid password")

else:
    print("weak password")


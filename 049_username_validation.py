#EXERCISE 1

#verify or validate username of a person. if space, if alphabet, if the length is >=6

username=input("enter username: ")


if username.isalpha():
    print("your username name is alphabetic")
    if not username.isspace():
        print("your username name is not spaced")
        if len(username)>=6:
            print("congrats. username is valid")



else:
    print("wrong username")




# method 2

username=input("enter username: ")

if username.islower() and username.isalpha() and len(username)>=6 and not username.isspace():
    print("\n\ncorrect password\n\n")
else:
    print("\n\nwrong password\n\n") 


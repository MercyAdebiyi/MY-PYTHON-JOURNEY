username= "Samson"
password= "ABC123"

person_username= input("enter your username: ").strip().title()
person_password= input("Enter your password: ").strip().upper()

if person_username==username and person_password==password:
    print("username and password is correct.")

elif person_username != username and person_password!=password:
     print("username and password is INcorrect.")

elif person_username != username and person_password==password:
     print("username is INCORRECT and password is correct.")

elif person_username == username and person_password!=password:
     print("username is CORRECT and password is INcorrect.")


else:
     print("enter valid email and password")


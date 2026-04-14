# Set a password (e.g. `"python123"`).
# Keep asking the user to enter the password until it is correct.

password= "Adebiyim008" 
user_password=input("Enter Your Password: ").strip().title()

while user_password !=password:
    print("Invalid Password")
    user_password=input("Enter Your Password: ").strip().title()


else:
    print("Password Accepted")
    
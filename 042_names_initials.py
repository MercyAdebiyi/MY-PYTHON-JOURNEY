first_name=input("enter your firstname: ").strip()
middle_name=input("enter your middlename: ").strip()
surname=input("enter your surname: ").strip()

print(f"\n\nHello {surname.capitalize()} {first_name[0].upper()}.{middle_name[0].upper()}\n\n")


print(f"\n\nHello {surname.capitalize()} {first_name[0:3].upper()}.{middle_name[::-1].upper()}\n\n")
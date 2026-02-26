number1= float(input("Enter your first number from 0-100: "))
number2= float(input("Enter your second number from 0-100: "))
operator= input("Enter an operator (+, -, *, /) to perform calculation: ").strip()

if operator== "+":
    print(number1 + number2)

elif operator== "-":
    print(number1 - number2)

elif operator== "*":
    print(number1 * number2)

else:
    print(number1 / number2)


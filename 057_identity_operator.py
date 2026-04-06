# OPERATORS REVISION

# 1. Assignment operators: =, +=, -=, *=. /=, %=, **=
# 2. Arithemetic operator: +, -, /, *, **, %
# 3. Comparison operatoes: ==, !=, >, <, >=, <=
# 4. Logical opeators: and, or, not
# 5. Membership operator: in
# 6. Identity operator: is


# The identity operator checks is the variable are the same AND in the same location

print("*************EXERCISE 1****************")

a = [10, 20, 30]
b = [10, 20, 30]
x=a

print(a == b)   # True  (same values)
print(a is b)   # False (different objects in memory)
print(x is a)

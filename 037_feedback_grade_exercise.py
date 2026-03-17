grade=(input("enter your grade eg: 'A', 'B', 'C', 'D', 'E', 'F': ")).strip().upper()

if grade== "A" or grade=="B":
    print("\nExcellent work\n")
else:
    if grade=="C":
        print("\nGood Effort\n")
    else:
        print("\nNeeds improvement\n")
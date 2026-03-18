battery=int(input("enter battery percentage: "))

if battery <=20:
    if battery <=5:
        print("\nCritical battery level\n")
    else:
        print("\nBattery Low\n")

else:
    print("\nBattery level is okay")
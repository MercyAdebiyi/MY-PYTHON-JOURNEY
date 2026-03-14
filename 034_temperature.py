temperature=int(input("enter today's temperate: "))

if temperature<20:
    if temperature<10:
        print("wear a heavy jacket.")
    else:
        print("wear a light jacket.")

else:
    print("No jacket needed.")
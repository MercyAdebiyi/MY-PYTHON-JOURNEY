print("--------SIMPLE EXERCISE-----------------")

print(f"\n\nPallandrome are words that mean the same thing when read from front and back. Eg (MOM)")
# name1, name2, name3, name4, age= "Oladimeji", "Mercy", "Zoe", "Tijesu", 26


word=input("Enter a word to see if it is a palladrome: ")
reverse_word=word[::-1]

if word==reverse_word:
    print("the word is a palladrome")
else:
    print("the word is NOT a pallandrome")
word=input("Enter a word: ")

vowel=("aeiou")
vowel_counter=0
i=0

while i<len(word):
    print(word[i])
    if word[i].lower() in vowel:
        vowel_counter+=1
    i+=1

print(f"word is {word}. It contains {vowel_counter} vowels")





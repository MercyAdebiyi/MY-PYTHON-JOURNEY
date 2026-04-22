word = input("Enter a word: ")

i = len(word) - 1

while i >= 0:
    print(word[i], end="")
    i -= 1

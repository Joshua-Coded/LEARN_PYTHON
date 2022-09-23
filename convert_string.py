orig_string = input("convert to acronuym: ")

orig_string = orig_string.upper()

list_of_words = orig_string.split()

for word in list_of_words:
    print(word[0], end="")
print()

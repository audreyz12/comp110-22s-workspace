"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730480148"

search_word: str = input("Enter a 5-character word: ")

if len(search_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

search_char: str = input("Enter a single character: ")

if len(search_char) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + search_char + " in " + search_word)

times_true: int = 0

if search_char == search_word[0]:
    print(search_char + " found at index 0")
    times_true = times_true + 1
if search_char == search_word[1]:
    print(search_char + " found at index 1")
    times_true = times_true + 1
if search_char == search_word[2]:
    print(search_char + " found at index 2")
    times_true = times_true + 1
if search_char == search_word[3]:
    print(search_char + " found at index 3")
    times_true = times_true + 1
if search_char == search_word[4]:
    print(search_char + " found at index 4")
    times_true = times_true + 1

if times_true == 1:
    print(str(times_true) + " instance of " + search_char + " found in " + search_word)
else:
    if times_true > 1:
        print(str(times_true) + " instances of " + search_char + " found in " + search_word)
    else: 
        print("No instances of " + search_char + " found in " + search_word)

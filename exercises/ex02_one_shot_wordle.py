"""EX02 - One-Shot Wordle - More progress toward Wordle."""

__author__ = "730480148"

# declare variables
secret: str = "python"
length: int = len(secret)
i: int = 0
boxes: str = ""
guess: str = input(f"What is your {length}-letter guess? ")

# if the guess is not the correct length, ask user to try again
while len(guess) != length:
    guess = input(f"That was not {length} letters! Try again: ")


while i < len(secret):
    # if the character guessed is correct and in the right position, add a green box
    if guess[i] == secret[i]:
        boxes += "\U0001F7E9"
    else:
        # if the character guessed is not correct and/or in the right position, 
        # check to see if the character guessed matches up with any character in the
        # secret word
        exists: bool = False
        alt: int = 0
        while alt < len(secret):
            # if the character guessed matches up with some character in the secret word
            # but is not in the correct position, notify the program that a yellow box should
            # be added
            if guess[i] == secret[alt]:
                exists = True
                alt = len(secret)
            else:
                alt += 1
        # add a yellow box if the character guessed exists in the secret word, but is not
        # in the correct position
        if exists:
            boxes += "\U0001F7E8"
        # if the character guessed isn't in the secret word at all, add a white box
        else:
            boxes += "\U00002B1C"
        alt = len(secret)    
    i += 1
print(boxes)

# tell the user if the guess is correct
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
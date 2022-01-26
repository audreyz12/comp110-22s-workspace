"""EX02 - One-Shot Wordle - More progress toward Wordle."""

__author__ = "730480148"

secret: str = "python"
length: int = len(secret)

guess: str = input(f"What is your {length}-letter guess? ")

while len(guess) != length:
    guess = input(f"That was not {length} letters! Try again: ")

i: int = 0
boxes: str = ""


while i < len(secret):
    if guess[i] == secret[i]:
        boxes = boxes + "\U0001F7E9"
    else:
        exists: bool = False
        alt: int = 0
        while alt < len(secret):
            if guess[i] == secret[alt]:
                exists = True
                alt = len(secret)
            else:
                alt = alt + 1
        if exists:
            boxes = boxes + "\U0001F7E8"
        else:
            boxes = boxes + "\U00002B1C"
        alt = len(secret)    
    i = i + 1

print(boxes)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
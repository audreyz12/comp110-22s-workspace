"""EX03 - Wordle - 6-guesses Wordle."""

__author__ = "730480148"


def contains_char(search_string: str, search_char: str) -> bool:
    """Returns True if the search character is found at any index of the first string."""
    assert len(search_char) == 1
    i: int = 0
    # index through the string being searched to see if the character being searched for
    # is present
    while i < len(search_string):
        if search_char == search_string[i]:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis depending on how close the guess is to the secret."""
    assert len(guess) == len(secret)
    i: int = 0
    boxes: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            # adds a green box if the character guessed exists and is in the same position 
            # in the secret word
            boxes += "\U0001F7E9"
        else:
            if contains_char(secret, guess[i]):
                # if the character exists but is not in the correct position, add a yellow box
                boxes += "\U0001F7E8"
            else:
                # if the character is not in the word at all, add a white box
                boxes += "\U00002B1C"
        i += 1
    return boxes
        

def input_guess(expected_length: int) -> str:
    """Returns the user's guess of length expected_length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    # checks if the guess is the same length as that of the secret word
    # if not, asks the user to try again
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    secret: str = "codes"
    game_on: bool = True
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            # if the guess is correct, end the game
            print(f"You won in {turns}/6 turns!")
            turns = 7
            game_on = False
        else:
            # if not, start another turn
            turns += 1
    if game_on:
        # if the player has not guessed the word correctly after 6 turns
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
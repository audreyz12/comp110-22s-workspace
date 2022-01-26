"""An example of conditional (if-else) statememts."""

"""all caps means you don't plan to change the variable"""
SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")
else: 
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

print("Game over.")
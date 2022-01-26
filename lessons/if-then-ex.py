"""Practice with if-then-else statements."""

choice: int = int(input("Enter a number: "))

# Implement this logic
# A < 25
# B >= 25 and < 50
# C > 75
# D >= 50 and <= 75

if choice >= 50:
    if choice > 75:
        print("C")
    else:
        print("D")
else:
    if choice < 25:
        print("A")
    else:
        print("B")
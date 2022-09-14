
import random

def roll():
    return random.randint(1, 6)

def rollTwo():
    die1 = roll()
    die2 = roll()
    sum = die1 + die2
    return "You Win!" if sum == 7 or sum == 11 else "Roll Again"

# Give it a try!
print(rollTwo())
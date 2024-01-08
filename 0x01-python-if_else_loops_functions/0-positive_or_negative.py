#!/usr/bin/python3
import random

# Assign a random signed number to the variable number
number = random.randint(-10, 10)

# Print the assigned number
print("The number is:", number)

# Assess if the number is positive, zero, negative
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")

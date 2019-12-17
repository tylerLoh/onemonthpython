""" to print squares of 1 to 10

we can use list or loop range 1 - 10
"""
import math

# list solution
numbers = list(range(1, 11))

for num in numbers:
    print(f"square for {num} is {num**2}")
    print(f"square root for {num} is {math.sqrt(num)}")

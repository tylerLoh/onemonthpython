""" Week 1: Lesson 4

This script allow the user to print to the console of random string
combination to the console
"""
import random

# List of first pair
bars = [
    "Lion's Head Tavern"
    "The Hamilton",
    "1020 Bar",
    "The Heights",
    "The Dead Poet",
    "Prohibition"
]

# List of friends name
people = [
    "Mattan",
    "Tyler",
    "Martin",
    "Alexander Hamilton",
    "Samuel L.Jackson",
    "Obama"
]

# pick random combination
random_bar = random.choice(bars)
random_person = random.sample(people, 2)

# python 3.6 introduce f-Strings format to improved String Formatting Syntax
# https://realpython.com/python-f-strings/
# print to console
print(f"How about you go to {random_bar} with {random_person[0]} "
      f"and {random_person[1]}")

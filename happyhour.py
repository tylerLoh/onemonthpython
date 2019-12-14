""" Week 1: Lesson 4

This script allow the user to print to the console of random string
combination to the console
"""
import random

# List of first pair
bars = ["Lion's Head Tavern"
        "The Hamilton",
        "1020 Bar",
        "The Heights",
        "The Dead Poet",
        "Prohibition"]

# List of friends name
people = ["Mattan",
          "Tyler",
          "Martin",
          "Alexander Hamilton",
          "Samule"]

# pick random combination
random_bar = random.choice(bars)
random_person = random.choice(people)

# print to console
print("How about you go to %s with %s" % (random_bar, random_person))

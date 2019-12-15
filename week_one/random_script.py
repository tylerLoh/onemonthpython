""" Week 1: Lesson 8

This one own implementation for random script
Ideally is to print random combination of string to console
"""
import random

# List of country name
countries = [
    "Malaysia",
    "England",
    "China",
    "United States",
    "Egypt",
    "Australia",
    "Italy",
    "Singapore",
    "Philippine"
]

# List of facts
facts = [
    "is good for coffee",
    "well diversified open economy across all markets globally",
    "has built many iconic buildings",
    "is most beautiful country to visit",
    "has the best street food",
    "is a good vacation spot",
    "has well-established transportation infrastructure in capital"
]

# random pick combination
country = random.choice(countries)
fact = random.choice(facts)

result = f"{country} {fact}"
print(result)

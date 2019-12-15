"""To capture user input from propmt terminal

built-int input() mtehod
"""

name = input("What's your name? ")
age = float(input("How old are you? "))
age_in_dog_years = age * 7

age_in_dog_years = int(age_in_dog_years) \
                   if age_in_dog_years % 1 == 0 \
                   else age_in_dog_years

print(f"{name} you are {age_in_dog_years} in dog years. Woof!")

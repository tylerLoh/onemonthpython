# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

a = [
    "FizzBuzz" if not i % 15
    else "Fizz" if not i % 3
    else "Buzz" if not i % 5
    else str(i)
    for i in range(1, 101)
    ]
print(' '.join(a))

"""Tip calculator

User enter bill amount and suggests few level tip amount to give

Bonus
-----
Can accpet dollar($) sign, use str.replace
"""

print("Welcome to Tip Calculator")
print("=========================")
print()

# To keep asking/capture user input until is a valid number
while True:

    bill_amount = input("Enter your bill amount: ")

    # replce dolalr sign
    bill_amount = bill_amount.replace("$", '')
    print()

    # try catch is a valid number
    try:
        bill_amount = float(bill_amount)
    except ValueError:
        print("!!! Input is not a valid number !!!")
        continue
    else:
        break

# tip level dict in percentage
tip_level = [15, 18, 20]

print("Bill tip recommendation:")
for level in tip_level:
    print(f"    {level}% = {level / 100 * bill_amount:.1f}")

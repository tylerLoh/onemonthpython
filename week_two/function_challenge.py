""" Week two function challeng

To upper case and reverse and args input
"""


def uppercase_and_reverse(text):
    """

    Parameters
    ----------
    text: str

    Returns
    -------
    str
        reverse and convert to uppercase
    """
    return text[::-1].upper()


print(uppercase_and_reverse('sab'))

a = [0, 1, 2, 3, 4]
print(a[:-3:-1])
# a[::-1] all items in the array, reversed
# a[1::-1] the first two items, reversed
# a[:-3:-1] the last two items, reversed
# a[-3::-1] everything except the last two items, reversed

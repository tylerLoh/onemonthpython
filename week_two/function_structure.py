""" Week two function structure
"""


def greet(name):
    """

    Parameters
    ----------
    name: str
        string of person name
    Returns
    -------
    tuple
        input name and 1
    string, int
        if left assignemnt(caller) match return args number
    """
    return name, 1


# same return args
a, b = greet('tyler')
print(b)

# diff return args
z = greet('tyler')
print(z)

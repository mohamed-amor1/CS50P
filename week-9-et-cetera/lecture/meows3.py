def meow(n: int) -> str:
    """
    Returns a string of 'meow' repeated n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A string of 'meow' repeated n times.
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

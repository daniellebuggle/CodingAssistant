"""
Write a Python program that compares two integers, a and b. Return:
    1 if a and b are equal
    2 if a is greater than b, or
    3 if b is greater than a
"""


def compare_integers(a, b):
    """
    Compares two integers, a and b.
    :param a: integer to compare
    :param b: integer to compare
    :return: integer - 1, 2, or 3
    """
    if a == b:
        return 1
    elif a > b:
        return 2
    else:
        return 3


def main():
    a = 100
    b = 44
    result = compare_integers(a, b)

    if result == 1:
        print("The integers are equal.")
    elif result == 2:
        print("The first integer is greater.")
    else:
        print("The second integer is greater.")


if __name__ == "__main__":
    main()

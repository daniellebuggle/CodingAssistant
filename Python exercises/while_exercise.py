"""
Write a program that calculates the factorial of a given number n using a while loop.
"""


def calculate_factorial(n):
    """
    Calculates the factorial of a given number.

    :param n: The number to calculate the factorial for (must be a non-negative integer)
    :return: The factorial of the number
    :raises ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial


def main():
    n = 5
    result = calculate_factorial(n)
    print(f"The factorial of {n} is: {result}")


# Run the main function
if __name__ == "__main__":
    main()

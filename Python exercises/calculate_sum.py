"""
Write a Python program that calculates the sum of all numbers in a given list. 
"""


def calculate_sum(numbers):
    """
    Calculates the sum of all numbers in a given list.

    :param numbers: List of numbers to sum up
    :return: The sum of the list
    """
    total_sum = 0
    for x in numbers:
        total_sum += x
    return total_sum


def main():
    numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]
    total_sum = calculate_sum(numbers)
    print("The sum of the list of numbers is:", total_sum)


# Run the main function
if __name__ == "__main__":
    main()

"""
Write a Python program that checks if a letter is a vowel ('a', 'e', 'i', 'o', or 'u').
"""


def is_vowel(letter):
    """
    Checks if a character is a vowel.
    :param letter: char to check
    :return: Boolean
    """
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or
            letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        return True

    return False


def main():
    letter = 'b'
    output = is_vowel(letter)
    print(output)


if __name__ == "__main__":
    main()

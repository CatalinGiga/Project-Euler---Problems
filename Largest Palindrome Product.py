# A palindromic muber reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(number: int) -> bool:
    """
    Checks if a number is a palindrome
    :param number: The number to check
    :return: True if the number is a palindrome, False otherwise
    """
    number = str(number)
    return number == number[::-1]


def largest_palindrome_product(digits: int) -> int:
    """
    Finds the largest palindrome made from the product of two n-digit numbers
    :param digits: The number of digits
    :return: The largest palindrome made from the product of two n-digit numbers
    """
    largest_palindrome = 0
    for i in range(10 ** (digits - 1), 10 ** digits):
        for j in range(10 ** (digits - 1), 10 ** digits):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome





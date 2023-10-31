# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def largest_prime_factor(number):
    """
    Finds the largest prime factor of a given number
    :param number: The number to find its largest prime factor
    :return: The largest prime factor of the given number
    """
    # Initialize the largest prime factor to 1
    largest_prime_factor = 1
    # Initialize the current factor to 2
    current_factor = 2
    # While the number is greater than 1
    while number > 1:
        # If the current factor divides the number
        if number % current_factor == 0:
            # Update the largest prime factor
            largest_prime_factor = current_factor
            # Divide the number by the current factor
            number //= current_factor
        else:
            # Increment the current factor
            current_factor += 1
    return largest_prime_factor

print(largest_prime_factor(600851475143))

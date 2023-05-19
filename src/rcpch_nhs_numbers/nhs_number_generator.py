from random import randint
from .nhs_number_validator import validate_nhs_number


def generate_nine_digits():
    """
    Generates a random 9 digit number and the remainder using the modulus 11 method
    """
    modulus_eleven = 0
    digit_string = ""
    for i in range(1, 10):
        # loop through the digits and apply multiplier which counts backwards from 11
        # then sum all the products
        multiplier = 11 - i
        # selects next digit in the number
        digit = randint(1, 9)  # int(f'{nine_digit_number}'[i - 1])
        modulus_eleven += digit * multiplier
        # divide the product by 11 and take the remainder
        digit_string += f"{digit}"
    remainder = modulus_eleven % 11
    return int(digit_string), remainder


def calculate_checksum(remainder):
    """
    Calculates the checksum from the remainder
    """
    # subtract remaind from 11 to get final checksum
    final_check_digit = 11 - remainder
    # if final_check_digit is 11, return 0. If 10, invalid
    if final_check_digit == 11:
        final_check_digit = 0
    elif final_check_digit == 10:
        return None

    return final_check_digit


def generate_nhs_number():
    """
    Generates a valid NHS number
    """
    final_check_digit = None

    while final_check_digit is None:
        # create a base 9 digit number, whose first digit cannot be < 1
        nine_digits, remainder = generate_nine_digits()
        # generate a checksum for that number - if None returned, number invalid, repeat
        final_check_digit = calculate_checksum(remainder)

    return int(f"{nine_digits}{final_check_digit}")


def generate_nhs_numbers(requested_number: int) -> list:
    """
    Returns a list of unique valid NHS numbers
    param: requested_number defines requested list length
    """
    number_set = set()
    failed_list = []
    while len(number_set) < requested_number:
        random_valid_nhs_number = generate_nhs_number()
        number_set.add(random_valid_nhs_number)

    return list(number_set)

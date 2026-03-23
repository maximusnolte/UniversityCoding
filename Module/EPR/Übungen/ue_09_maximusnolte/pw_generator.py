__author__ = "MatrNr, Nachname"

"""
Password generator logic.
"""

import random
import string


def generate_password(length: int,
                      use_lower: bool = True,
                      use_upper: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = False) -> str:
    """
    Generate a random password.

    :param length: Length of the password
    :param use_lower: Use lowercase letters
    :param use_upper: Use uppercase letters
    :param use_digits: Use digits
    :param use_symbols: Use special characters
    :return: Generated password
    :raises ValueError: If no character set is selected
    """
    charset = ""

    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    if not charset:
        raise ValueError("At least one character set must be selected.")

    return "".join(random.choice(charset) for _ in range(length))

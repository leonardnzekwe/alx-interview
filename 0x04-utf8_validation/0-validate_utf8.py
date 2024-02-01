#!/usr/bin/python3
"""
UTF-8 Validation Module.
Determines if a given data set represents a valid UTF-8 encoding.
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Validates if the given data is a valid UTF-8 encoding.

    :param data: List of integers representing 1 byte of data each.
    :return: True if data is a valid UTF-8 encoding, else return False.
    """
    # Variable to keep track of the number
    # of remaining bytes for the current character
    remaining_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # Convert the byte to binary and make sure it's 8 bits long
        binary_representation = bin(byte)[2:].zfill(8)

        # Check the first few bits to determine the type of character
        if binary_representation.startswith("0") and remaining_bytes == 0:
            # Single-byte character (ASCII)
            continue
        elif binary_representation.startswith("110") and remaining_bytes == 0:
            # Start of a 2-byte character
            remaining_bytes = 1
        elif binary_representation.startswith("1110") and remaining_bytes == 0:
            # Start of a 3-byte character
            remaining_bytes = 2
        elif (
            binary_representation.startswith("11110") and remaining_bytes == 0
          ):
            # Start of a 4-byte character
            remaining_bytes = 3
        elif binary_representation.startswith("10") and remaining_bytes > 0:
            # Continuation byte
            remaining_bytes -= 1
        else:
            # Invalid starting bits for a character
            return False

    # If we've processed all bytes and
    # the remaining_bytes is 0, it's valid UTF-8
    return remaining_bytes == 0

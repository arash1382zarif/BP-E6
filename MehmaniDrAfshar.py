#!/usr/bin/env python3
# Author: Arash Zarif

def get_int_input(prompt):
    """Get integer input from the user."""
    return int(input(prompt))


def convert_to_binary_string(number):
    """Convert an integer to a 32-bit binary string."""
    binary_representation = bin(number)[2:]
    return (32 - len(binary_representation)) * "0" + binary_representation


def check_bit_at_index(binary_string, index):
    """Check if the bit at a specific index in the binary string is '1'."""
    return binary_string[63 - index] == "1"


def main():
    # Get input values
    right = get_int_input("")
    left = get_int_input("")

    # Convert to binary strings
    binary_right = convert_to_binary_string(right)
    binary_left = convert_to_binary_string(left)

    # Concatenate binary strings
    binary_string = binary_left + binary_right

    # Number of queries
    n = get_int_input("")

    # Check bits at specified indices
    for _ in range(n):
        index = get_int_input("")
        if check_bit_at_index(binary_string, index):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()

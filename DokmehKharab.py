#!/usr/bin/env python3
# Author: Arash Zarif

def get_int_input(prompt):
    """Get integer input from the user."""
    return int(input(prompt))


def calculate_sum_and_carry(m, n):
    """Calculate the sum and carry of two integers."""
    while n != 0:
        carry = m & n
        m = m ^ n
        n = carry << 1
    return m


def main():
    # Get input values
    m = get_int_input("")
    n = get_int_input("")
    k = get_int_input("")

    # Calculate sum and carry
    result = calculate_sum_and_carry(m, n)

    # Check if result equals k
    if k == result:
        print(result)
        print("YES")
    else:
        print(result)
        print("NO")


if __name__ == "__main__":
    main()

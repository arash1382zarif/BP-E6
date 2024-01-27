def get_int_input(prompt):
    """Get integer input from the user."""
    return int(input(prompt))


def count_set_bits(a, b):
    """Count the number of set bits in the XOR of two integers."""
    xor_result = a ^ b
    bit_count = 0
    while xor_result:
        bit_count += xor_result % 2
        xor_result //= 2
    return bit_count


def main():
    # Get input values
    a = get_int_input("")
    b = get_int_input("")

    # Count set bits in XOR result
    result = count_set_bits(a, b)

    print(result)


if __name__ == "__main__":
    main()

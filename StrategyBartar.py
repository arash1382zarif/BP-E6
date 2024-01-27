#!/usr/bin/env python3
# Author: Arash Zarif

def get_input():
    """Get space-separated integers as input."""
    return map(int, input().split())


def is_prime(num):
    """Check if a number is prime."""
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False


def main():
    # Get input values
    a, b = get_input()

    # Ensure a is less than or equal to b
    if a > b:
        a, b = b, a
        print('reverse order - amount: ', end='')
    else:
        print('main order - amount: ', end='')

    # Count prime numbers in the range [a, b]
    count = sum(1 for x in range(a, b + 1) if is_prime(x))

    print(count)


if __name__ == "__main__":
    main()

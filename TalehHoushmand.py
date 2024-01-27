#!/usr/bin/env python3
# Author: Arash Zarif

def sum_of_divisors(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)


def number_to_base(n, base):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % base))
        n //= base
    return digits[::-1]


def main():
    total_sum = 0
    flag = True

    while True:
        n, b = map(int, input().split())

        if n == -1 and b == -1:
            break

        if b < 2 or b > 9:
            print("invalid base!")
            flag = False
            break

        x = ''
        digits = number_to_base(sum_of_divisors(n), b)

        for digit in digits:
            x += str(digit)

        total_sum += int(x)

    if flag:
        print(total_sum)


if __name__ == "__main__":
    main()

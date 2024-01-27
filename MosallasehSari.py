def get_int_input(prompt):
    return int(input(prompt))


def generate_pascal_triangle(n):
    """Generate Pascal's Triangle up to the nth row."""
    for line in range(1, n + 1):
        coefficient = 1
        for i in range(1, line + 1):
            print(coefficient, end=" ")
            coefficient = int(coefficient * (line - i) / i)
        print("")


def main():
    n = get_int_input("")
    generate_pascal_triangle(n)


if __name__ == "__main__":
    main()

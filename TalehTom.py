def get_input_numbers():
    """Get user input for numbers until 'end' is entered."""
    numbers = []
    while True:
        num = input()
        if num.lower() == "end":
            break
        numbers.append(int(num))
    return numbers


def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    try:
        return round(sum(numbers) / len(numbers), 2)
    except ZeroDivisionError:
        return 0


def calculate_lcm_of_array(arr, idx):
    """Calculate the least common multiple of an array of numbers."""
    if idx == len(arr) - 1:
        return arr[idx]
    a = arr[idx]
    b = calculate_lcm_of_array(arr, idx + 1)
    return int(a * b / gcd(a, b))


def calculate_gcd_of_array(array):
    """Calculate the greatest common divisor of an array of numbers."""
    gcd_num = gcd(array[0], array[1])
    for i in range(1, len(array)):
        gcd_num = gcd(gcd_num, array[i])
    return gcd_num


def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    result = min(a, b)
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result


def main():
    commands = ["sum", "average", "lcd", "gcd", "min", "max"]
    operation = input().lower()

    if operation not in commands:
        print("Invalid command")
    else:
        numbers = get_input_numbers()

        if operation == "sum":
            print(calculate_sum(numbers))
        elif operation == "average":
            print(calculate_average(numbers))
        elif operation == "lcd":
            print(calculate_lcm_of_array(numbers, 0))
        elif operation == "gcd":
            print(calculate_gcd_of_array(numbers))
        elif operation == "min":
            try:
                print(min(numbers))
            except ValueError:
                print(0)
        elif operation == "max":
            try:
                print(max(numbers))
            except ValueError:
                print(0)


if __name__ == "__main__":
    main()

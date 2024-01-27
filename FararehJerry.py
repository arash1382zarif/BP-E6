def get_input(prmopt):
    """Get user input."""
    return input(prmopt).strip()


def create_empty_map(n):
    """Create an empty map of size n."""
    return ["." * n]


def update_map(my_map, height, x):
    """Update the map based on user input."""
    my_map[height] = my_map[height][:x] + "*" + my_map[height][x + 1:]


def print_map(my_map, height):
    """Print the map up to the specified height."""
    for i in range(height + 1):
        print(" ".join(my_map[i]))


def main():
    n = int(get_input(""))
    height = 0
    x = 0

    my_map = create_empty_map(n)

    while True:
        input_str = get_input("")

        if input_str == 'B':
            height += 1
            my_map.append(n * '.')

        if input_str == 'R':
            x = min(x + 1, n - 1)

        if input_str == 'L':
            x = max(x - 1, 0)

        update_map(my_map, height, x)

        if input_str == "END":
            break

    print_map(my_map, height)

    if x != n - 1:
        print("There's no way out!")


if __name__ == "__main__":
    main()

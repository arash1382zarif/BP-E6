def decrypt_codes(codes):
    decrypt = [0] * len(codes)

    for code in codes:
        char = code[0]
        idx = int(code[1:])
        decrypt[idx] = char

    return "".join(str(char) for char in decrypt)


def main():
    codes = input().split()
    result = decrypt_codes(codes)
    print(result)


if __name__ == "__main__":
    main()

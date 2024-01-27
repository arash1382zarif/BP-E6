codes = input().split()
decrypt = [0] * len(codes)

for code in codes:
    char = code[0]
    idx = int(code[1:])
    decrypt[idx] = char

print("".join(decrypt))
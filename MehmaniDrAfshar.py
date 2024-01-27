right = int(input())
left = int(input())
binary_right = bin(right).replace("0b", "")
binary_left = bin(left).replace("0b", "")
binary_right = (32 - len(binary_right)) * "0" + binary_right
binary_left = (32 - len(binary_left)) * "0" + binary_left
binary_string = binary_left + binary_right
n = int(input())
for i in range(n):
    index = int(input())
    if binary_string[63-index] == "1":
        print("yes")
    else:
        print("no")

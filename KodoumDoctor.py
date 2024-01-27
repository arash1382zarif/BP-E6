a = int(input(""))
b = int(input(""))
x = a ^ b
counter  = 0
while x >= 1:
    k = x % 2
    if k == 1:
        counter += 1
    x = int(x / 2)
print(counter)


m = int(input(""))
n = int(input(""))
k = int(input(""))
while (n != 0):
    carry = m & n
    m = m ^ n
    n = carry << 1

if k == m:
    print(k)
    print("YES")
else:
    print(m)
    print("NO")


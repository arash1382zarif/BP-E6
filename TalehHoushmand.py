def sum_of_numerators(n):
    sum = 0
    for i in range(1,n + 1):
        if (n % i == 0):
            sum += i
    return sum

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

n = 0
b = 0
sum = 0
flag = True
while(True):
    n, b = map(int,input().split())

    if (n == -1 and b == -1):
        break

    if (b < 2 or b > 9):
        print("invalid base!")
        flag = False
        break

    x = ''

    digits = numberToBase(sum_of_numerators(n), b)

    for i in range(len(digits)):
        x += str(digits[i])

    sum += int(x)

if (flag):
    print(sum) 




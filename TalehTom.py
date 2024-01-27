import math

operation = input()
commands = ["sum", "average", "lcd", "gcd", "min", "max"]
def gcd(a, b):
    result = min(a, b)
 
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result

def gcdN(array): 
    gcd_num = gcd(array[0], array[1])
    for i in range(1, len(array)):
        gcd_num = gcd(gcd_num, array[i])
    
    return gcd_num
def LcmOfArray(arr, idx):
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx+1)
    return int(a*b/ gcd(a,b))

if (operation not in commands):
    print("Invalid command")
else:
    numbers = []
    while True:
        num = input()
        if (num == "end"):
            break
        numbers.append(int(num))

    if (operation == "sum"):
        print(sum(numbers))
    elif (operation == "average"):
        try:
            print(round(sum(numbers)/len(numbers), 2))
        except ZeroDivisionError:
            print(0)
    elif (operation == "lcd"):
            print(LcmOfArray(numbers, 0 ))
    elif (operation == "gcd"):
            print(gcdN(numbers))

    elif (operation == "min"):
        try:
            print(min(numbers))
        except:
            print(0)
    elif (operation == "max"):
        try:
            print(max(numbers))
        except:
            print(0)
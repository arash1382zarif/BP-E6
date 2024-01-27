def printPairs(arr, sum):
    res = []
    s = set()
    for i in range(len(arr)):
        temp = sum - arr[i]
        if (temp in s):
            res.append(arr.index(temp)+i)
        s.add(arr[i])
    return res

lst = input().strip().split(" ")
lst = [int(x) for x in lst]
n = len(lst)
target = int(input())

res = printPairs(lst, target)

if (len(res) == 0):
     print("Not Found!")
else:
     res = sorted(res)
     for i in res:
          print(i)
inp = (input()).split(" ")
a, b = int(inp[0]), int(inp[1])
if a > b:
   c = b
   b = a
   a = c
   print('reverse order - amount: ', end='')
else:
   print('main order - amount: ', end='')
count = 0
for x in range(a, b+1):
  if x>1:
      yN = False
      for i in range(2 , x):
          if (x % i) == 0:
            yN = True
            break
      if yN == False:
        count+=1
print(count)
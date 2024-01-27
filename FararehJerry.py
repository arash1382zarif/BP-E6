n = 0
n = int(input())
input_str = ''
height = 0
x = 0

map = []

    
map.append("." * n)

map[0] = map[0][:0] + "*" + map[0][1:]

while(True):
    input_str = input()
    input_str = input_str.strip()
    if (input_str == 'B'):
        height += 1
        map.append(n * '.')
    if (input_str == 'R'):
        x += 1
        if (x > n - 1):
            x = n - 1
    if (input_str == 'L'):
        x -= 1
        if (x < 0):
            x = 0
    

    map[height] = map[height][:x] + "*" + map[height][x+1:]

    if (input_str == "END"):
        break

for i in range(height + 1):
    for j in range(n):
        print(map[i][j], end=' ')
    print()
if (x != n -1):
    print("There's no way out!")

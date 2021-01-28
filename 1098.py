h, w = map(int, input().split())
r = [[0]*w for _ in range(h)]
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(int(l)):
        r[x-1][y-1] = 1
        if d == 0:
            y += 1
        else:
            x += 1
for i in r:
    for j in i:
        print(int(j), end=' ')
    print()
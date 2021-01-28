n = int(input())
r = [[0] * 19 for i in range(19)]
for i in range(n):
    x, y = map(int, input().split())
    r[x - 1][y - 1] = 1#실제 입력받는 값과 리스트값은 -1차이가 있다! 잘보기!
for i in r:
    for j in i:
        print(j, end=' ')
    print()

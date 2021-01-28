r = [[0]*10 for _ in range(10)] #어떠한 변수가 마땅히 필요없을때  for _ in range를 사용한다.
for i in range(0, 10): #0부터 9까지 총 10번 반복하라는 의미로 range(10)을 사용해도됨
    r[i] = input().split() #r=list(map(int,input().split()))은 리스트로 저장xx 컴파일 에러남!!
x = 1
y = 1
while True: #무한루프 구문으로 빠져나가기 위해서 break사용!!, 끝까지 r[x][y]가 2가 나오지 않는 경우도 존재하므로 이를 조건으로 사용xx
    if r[x][y] == '2':#콤마 포함하기
        r[x][y] = '9'
        break
    r[x][y]='9'
    if r[x][y+1] == '2':
        r[x][y+1] = '9'
        break
    elif r[x][y + 1] == '0':
        y += 1
    elif r[x+1][y] == '0':
        x += 1
    elif r[x+1][y] == '2':
        r[x + 1][y] = '9'
        break
    elif r[x+1][y] == '1' and r[x][y+1] == '1':#오른쪽, 아래쪽 다 막힌상황
        break
    else:
        break
for i in r:
    for j in i:
        print(int(j), end=' ')
    print()
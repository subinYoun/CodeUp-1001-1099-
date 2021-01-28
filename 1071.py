#0 입력될 때까지 무한 출력하기
a = map(int, input().split())
for i in a:
    if i == 0:
        break
    print(i)#콤마 포함하면 i가 그대로 출력됨
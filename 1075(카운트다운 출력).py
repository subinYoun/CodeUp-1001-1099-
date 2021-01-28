#정수 1개 입력받아 카운트다운 출력하기
a = int(input())
for i in range(a-1, -1, -1): #1씩 줄이면서 0이 될 때까지 출력
    print(i)
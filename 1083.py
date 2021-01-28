#1083. 369게임
a=int(input())
for i in range(1, a+1):
    if i==3 or i==6 or i==9:#i%3==0으로 표현하면 더 짧은 코드 가능
        print("X", end=' ') #나란히 반복해서 같은 줄에 출력하고 싶을 때 end=' ' 사용! ''사이에는 각 출력들 사이에 들어갈 것
    else:
        print(i, end=' ')
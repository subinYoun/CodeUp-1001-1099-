#출석을 부른 번호 순서 바꾸어 출력하기
n=int(input())
a=list(map(int, input().split()))
for i in range(n):#range(n)이 아닌 a는 불가능
    print(a[n-int(i)-1], end=' ')
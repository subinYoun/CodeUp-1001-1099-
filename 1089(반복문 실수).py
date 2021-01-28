#수 나열하기
a, b, c=map(int, input().split())#시작값, 등차값, 몇번째 수
for i in range(c-1):#0부터 c-1까지 c번 반복
    a += b
print(a)
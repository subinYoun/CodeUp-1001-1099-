a, b, c=map(int, input().split())
r=0
for i in range(0, a):
    for j in range(0, b):
        for k in range(0, c):
            print(i,j,k) #변수 i, j, k를 r, g, b와 같은 변수로 코드를 짜니 오답이 출력되었다. 이유는 모르겠음
            r+=1
print(r)
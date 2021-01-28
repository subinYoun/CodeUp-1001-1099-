a=int(input())
b=input().split()
r=[0]*23#밑에 range범위 2번째 따름
for i in range(0,23):
    for j in b:
        if int(i)==int(j)-1:
            r[i]+=1
    print(r[i], end=' ')
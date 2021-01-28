n=int(input())
a=input().split()
result=[0]*23
for i in range(n):
    result[int(a[i])-1]+=1
for p in result:
    print(p, end=' ')

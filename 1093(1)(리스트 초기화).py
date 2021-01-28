#이상한 출석부 부르기
a=int(input())#출석부 부른 횟수
b=input().split()#무작위로 부른 a개의 번호
r=[0]*24#23개의 리스트->밑에 범위 두번째 따름
for i in range(1,24):
    for j in b:
        if int(i)==int(j):#int를 붙여야함
            r[i]+=1
    print(r[i], end=' ')
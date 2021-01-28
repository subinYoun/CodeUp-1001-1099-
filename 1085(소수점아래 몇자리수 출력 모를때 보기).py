a, b, c, d= map(int, input().split())
r=(((a*b*c*d)/8)/1024)/1024
print(round(r, 1),"MB")#소수점 아래 두번째자리에서 반올림하여 한자리수까지 출력된다.
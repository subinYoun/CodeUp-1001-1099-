#그림 파일 저장용량 계산하기
a, b, c=map(int, input().split())
r=(((a*b*c)/8)/1024)/1024
print("%.2f MB" %r)#소수점 반올림은 2d가 아니라 2f
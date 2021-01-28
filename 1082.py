#16진수 구구단
a=input()
n=int(a, 16)
for i in range(1, 16):
    print("%X*%X=%X" %(n, i, n*i)) #%X는 16진수로 출력해주는 기호(외울것!!)
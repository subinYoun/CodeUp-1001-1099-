#1080.언제까지 더해야 할까?(입력이 도출될때까지 계속 더해주고 마지막에 더해준 값을 출력한다.
#입력 예시: 55 ->출력 예시: 10
a=input()

n=int(a)

i=0
s=0
while s < n: #s의 값이 n이 될 때까지 더해주는 것이므로 s<n을 해주면 마지막 반복문이 실행될때 s값이 목표치(n)에 도달하게 된다
    i += 1
    s += i

print(i)
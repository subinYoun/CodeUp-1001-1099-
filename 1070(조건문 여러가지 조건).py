#월 입력받아 계절 출력하기
a = int(input())
if a == 12 or a == 1 or a == 2:#a==12, 1, 2 불가능! 따로 써줘야함
    print("winter")
elif a == 3 or a == 4 or a == 5:
    print("spring")
elif a == 6 or a == 7 or a == 8:
    print("summer")
else:
    print("fall")
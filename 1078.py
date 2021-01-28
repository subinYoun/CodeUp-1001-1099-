a=input("")
result=0
i=0 #이것이 없으면 안됨
while i <= int(a):
    if i%2 == 0:
        result += i
    i += 1
print(result)
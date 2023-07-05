list = []
for _ in range(10):
    list.append(int(input()))

#입력값은 10개이고 중간에 끊으면 끝이니 for 문으로 간단하게 가보자

temp=0
result=0
pre_temp = 0
for i in range(10):
    pre_temp = temp
    temp += list[i]
    if temp == 100:
        result = temp
        break
    if abs(100-temp)<=abs(100-pre_temp):
        result = temp


print (result)

#더하기 사이클, 조금 복잡한데? 이해만 하면 될듯
#그냥 while 문 돌려도 입력값이 작아서 괜찮을거같은데
#한자리 숫자면 0을 붙이고, 아니면 그냥 분리해서 b + (a+b). 
#9 +9 인 18이 최대겠네
n = int(input())
ans = n #정답 대조용
count = 0 #최종출력용
a= 0
b = 0
while True :
    count+=1
    if n <10: #숫자 분리용. 
        a = 0
        b = n
    else:
        a = n //10
        b = n %10
    c = (a+b)%10 #1의자리수
    n = (b*10)+c
    if n == ans :
        break
print(count)
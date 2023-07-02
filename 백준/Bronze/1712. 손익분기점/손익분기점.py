#A 고정비용 B 가변비용 C가격
#그냥 반복문으로 풀기엔..21억이라 불가능
#수학적으로 a+b //c 고 나머지가 있는경우 +1 할까?

#문제를 잘못이해. a + b*ans //ans 임. 
#생산수에 따라 손익분기점이 바뀜.
#손익분기점이 존재하지 않는 경우는 b가 c보다 클때
#흠... 우선 C로 A 만큼 번 다음... 그냥 B랑 C의 차액만큼인거같은데

a,b,c = map(int,input().split())
if b>c or b==c :
    print(-1)
else :
    p = abs(b-c) #차액
    ans = a//p +1
    print(ans)
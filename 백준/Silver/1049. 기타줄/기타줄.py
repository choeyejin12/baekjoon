#기타줄 n 개가 끊어졌다. 되도록 돈을 적개 == 그리디
#기타줄 브랜드 m 개 만큼 주어짐.
#16개 짜리 값, 1개 값
#입력값도 크지 않음
#흠...그리디니까... 6개들이가 더 싼데 1개짜린 비싼경우나, 1개짜린 싼데 6개짜리가 비싼경우...
#이러한예외를 제외하고 만약 n 이 6보다 높다면 6개짜리중 가장 싼거와 낱개별 6개중 가장싼거..?
#그 외에는 각각 가장 작은 숫자중 1/6 한거와 1개의 가격을 비교하면된다.

#잠깐만 생각이상으로 더 간단한데? 그냥 제일싼 세트값이랑 제일 싼 개별줄 중에 개당 싼걸로 하고,,,
#아 그러면 안되네 ㅎ

n,m = map(int,input().split())
das = [] #기타줄 set
one = [] #기타줄 하나
ans = 0 #출력용 정답
for _ in range(m):
    a,b = map(int,input().split())
    das.append(a)
    one.append(b)

das.sort()
one.sort()

while n > 0:

    if n >=6 :#클때는 다스랑 개별값 비교
        if das[0] <=(one[0]*6):
            n -= 6
            ans += das[0]
        else :
            ans += (6*one[0])
            n -=6
    else: #크지않을때는 개별과 나눗셈값 비교
        if das[0] <(n*one[0]):
            ans += das[0]
            n = 0
        else:
            ans += n*one[0]
            n = 0

print(ans)
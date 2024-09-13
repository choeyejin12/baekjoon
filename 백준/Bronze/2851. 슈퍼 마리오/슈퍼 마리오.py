#너무 더럽게 풀었다. 어렵지 않은 문제인데 괜히 dp 쓴다고...
#정신차리고 쉬운건 쉽게 풀고 넘어가자. 반복문 상태에서 100을 뺀 절댓값을 기준으로 하면된다.
#슈퍼마리오. 생각보다 간단할거같긴한데.... 입력값이 10개니 반복문으로 풀어도 괜찮을것같다
#다이나믹 프로그래밍을 살짝 응용해서...?
#network = [[]*(N+1) for _ in range(N+1)] 
'''
mush = []
for _ in range(10):
    mush.append(int(input()))#버섯 리스트
dp = [mush[0]]

for i in range(1,10):
    a = (dp[i-1]+mush[i])
    dp.append(a) #모든 덧샘수 넣기
m = 0
dps= [] 
#얕은복사, 1차원이면 괜찮은데 2차원 객체면 id 가 같아서 안됨. 1차원이니 쓰자
for j in range(10):
    d = dp[j]
    dps.append(abs(d-100))
mini = min(dps)
m = dps.index(mini)
#정수랬으니 0 은 없겠지... 
dps[m]= 100000000
if mini in dps:
    m = dps.index(mini)

print(dp[m])

'''

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
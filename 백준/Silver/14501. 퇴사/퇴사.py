#힌트는 뒤에서 부터 확인하는 것이었다. 마지막 날의 [i][1]이 i+n을 넘으면 제외한다.
#개미 전사와 비슷하게 
n = int(input())
time = []
price = []
dp = [] #dp 메모리제이션
for i in range(n):
    x,y = map(int,input().split())
    time.append(x)
    price.append(y) #입력 완료
    dp.append(y)#dp 를 출력하고결국 최종프라이스 합을 내기 떄문
dp.append(0)

for i in range( n-1 ,-1 ,-1):
    if time[i]+i > n :
        dp[i] = dp[i+1]
    else:
        dp[i]=max(dp[i+1], price[i]+dp[i+time[i]])

print(dp[0])
n =int(input())
P = list(map(int,input().split()))
tim = 0
wait= 0
P.sort()
for _ in range(n):
    wait += P[_]
    tim += wait
print (tim)
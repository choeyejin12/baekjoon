tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int,input().split()) 
ans = " "
while n != 0:
    ans +=str(tmp[n%b])
    n = n//b

print(ans[::-1])#거꾸로 출력 
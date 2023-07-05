n =int(input())
lis = []
for _ in range(n):
    lis.append(int(input()))
lis.sort()
for _ in range(n):
    print(lis[_])
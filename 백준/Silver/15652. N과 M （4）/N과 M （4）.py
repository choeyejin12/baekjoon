from itertools import combinations_with_replacement
from itertools import product

n,m = list(map(int,input().split()))
 
s = []
 
for _ in range(1,n+1):
    s.append(_)
def dfs():
    if len(s)==m: # 조건 m 자리수 만큼에 부합하는지. 부합하면 출력후 함수초기화
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        #if i not in s:
        s.append(i)
        dfs()
        s.pop()

for i in combinations_with_replacement(s,m):
    for j in i:
        print(j,end=" ")
    print("")
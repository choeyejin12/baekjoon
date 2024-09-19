n,m = list(map(int,input().split()))
list = list(map(int,input().split()))
list.sort()
s = []
 

def dfs():
    if len(s)==m: # 조건 m 자리수 만큼에 부합하는지. 부합하면 출력후 함수초기화
        print(' '.join(map(str,s)))
        return
    
    for i in list:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
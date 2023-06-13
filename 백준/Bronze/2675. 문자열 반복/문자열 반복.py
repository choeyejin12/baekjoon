n = int(input())

for _ in range(n):
    r,s = map(str,input().split())
    texr = ""
    r = int(r)
    for i in s:
        print(i*r,end="")#는 틀렸음 끝에 % 때문에..? 모르겟다
        #texr +=i*r
    print()   
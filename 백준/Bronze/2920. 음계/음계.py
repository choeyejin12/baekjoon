S = list(map(int,input().split()))

if S == sorted(S):
    print("ascending")
elif S == sorted(S,reverse = True):
    print("descending")
else:
    print("mixed")
import sys

n = int(sys.stdin.readline())
#이중 리스트 만들기?
xylist = []
for _ in range(n):
    xylist.append(list(map(int,sys.stdin.readline().split())))
xylist = sorted(xylist)

for _ in range(n) :
    print(xylist[_][0],xylist[_][1])
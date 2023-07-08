import sys

x = int(sys.stdin.readline())
n = []
for _ in range(x):
    n.append(int(sys.stdin.readline()))
list = sorted(n)
for _ in range(x):
    print(list[_])
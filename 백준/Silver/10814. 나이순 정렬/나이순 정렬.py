n = int(input())
list1 = []
for i in range(n):
    list1.append(list(input().split()))
list1.sort(key=lambda x :int( x[0]))
for i in range(n):
    print(list1[i][0],list1[i][1])
x,y , w, h = map(int,input().split())

x1 = (w-x)
y1 = (h-y)
if (x1 <x)and(y1<y):
    print(min(x1,y1))
else:
    print(min(x1,y1,x,y))
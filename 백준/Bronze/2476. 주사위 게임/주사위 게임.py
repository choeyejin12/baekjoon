n = int(input())#참여자
nlist =[]#상금리스트

for _ in range(n):
  prize =0#가장큰상금,초기화
  a,b,c = map(int,input().split())
  if a == b and b== c and a==c:
    prize =(10000+a*1000)
    nlist.append(prize)
  if a == b :
    prize =(1000+a*100)
    nlist.append(prize)
  if a == c :
    prize =(1000+a*100)
    nlist.append(prize)

  if c == b :
    prize =(1000+b*100)
    nlist.append(prize)

  else:
    prize = 100*max(a,b,c)
    nlist.append(prize)

print(max(nlist))
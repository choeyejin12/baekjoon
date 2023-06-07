#아스키코드로 할까?

string = str(input())

aski = [0]*100

string = string.upper()
for i in string:
    a = ord(i)
    aski[a] += 1

maxi = max(aski)
maxa = aski.index(maxi)
askis = aski[maxa+1:]
if maxi in askis:
    print("?")
else:
    
    print(chr(maxa))
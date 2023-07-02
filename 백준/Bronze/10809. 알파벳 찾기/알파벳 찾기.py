#우선 출력용으로 배열을 하나 만들고,,, ans
#해당 숫자가 등장하면 처음 등장하는 위치 인덱스.
#없으면 -1. 출력은 공백을 넣어서
#먼저 확인할 문자의 인덱스를 apb에서 찾고, 입력문중 문자의 인덱스를 ans[apb] 에 넣는다.
stri = str(input())
ans = [-1]*26 #정답 출력용 배열
#아스키 코드로 변환해서 해당 위치에 더하기...도 낫지만 그냥 이렇게 가자
apb = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(len(stri)):
    a = stri[i] # 확인할 문자
    ap = apb.index(a) #확인된 문자의 알파벳순서
    ans[ap] = stri.index(a)

print(*ans,sep=" ")
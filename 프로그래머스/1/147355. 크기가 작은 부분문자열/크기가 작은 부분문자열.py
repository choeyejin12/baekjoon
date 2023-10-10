#브루트 포스 조합? 
#zip 이나 itertools 를 쓰면...
#간단히 len(p) 만큼의 자릿수를 잘라 t에서 문자열을 만들고
#그 문자열 중 p 보다 숫자가 작은 문자열을 찾으면된다.
#아까 공부한 zip 을 응용해보자.
#의 길이만큼 앞에서 없앤 리스트를 만들어서...zip... 
#p 의 길이는 18이니 괜찮나? 
#근데 이러면 zip이 어렵다.
def solution(t, p):
    answer = 0
    n = len(p) #이만큼 조합을 구한다.
    m = len(t)-n
    #nlist =[]#길이 n의 순열이 들어갈 배열
    cnt =0 #답
    for i in range(m+1):
        a = t[i:i+n]

        if int(a) <= int(p):
            cnt+=1
    print(cnt)
        
    return cnt
#ptsd 오는 기본적인 문제!!!!!! 이건 꼭 풀어야해
#회전? 시켰을때? 그러니까 1차원 앞뒤가 이어진 형태일때.
#왼쪽으로 회전시키면 0번쨰 인덱스가 마지막 인덱스가 되고 인덱스 -1씩 하고 0번쨰는 마지막 인덱스로 붙이면 된다.
#이 회전을 len(s) 만큼 시킨다. 이때 생기는 올바른 괄호 문자는 몇번 나오는지 확인하시오
#올바른 괄호 문자열의 조건은 모든문자열이 말이 되어야한다.
#괄호안에 괄호가 있어도 가능하므로 이 괄호는 스택으로 구현하자
#하나라도 잘못된 괄호가 있다면 바로 break 한다.

#그럼 괄호 문자열이 생기는지 보는 함수와 돌리는 함수를 이용하자
#돌리는건 큐를 이용해야할거같은데

def gwal(s):
    
    start = "[({"
    end = "])}"
    sg =[] #지금 괄호 넣어둘꺼
    for i in s:
        if i in start : #여는 괄호일때
            sg.append(i) #지금 괄호 상태에 넣기
            continue
            
        elif i in end and len(sg)==0: #닫는 괄호고 현재 괄호가 빈칸이면
            return 0
            break

            
        else: #여는 괄호 아니고 닫는 괄호인데 sg 에 여는 괄호가 있을 때.
            a = sg.pop()
            a = start.index(a) #현재 괄호의 순서에 맞는 닫는 괄호가 아니면
            if i == end[a]:
                continue
            else:
                return 0
                break
    if len(sg) > 0 :
        return 0

    return 1
        
def solution(s):
    answer = 0 #올바른 문자열이 생기면 +1
    
    s=list(s)
    ls = len(s)
    if ls == 1:
        return 0
        

    if gwal(s) == 1:
        answer +=1

    for _ in range(ls-1):
        
        tmp = s.pop(0)
        s.append(tmp) #이렇게 돌려
        if gwal(s) == 1:
            answer +=1
        else :
            continue
    
            
    return answer
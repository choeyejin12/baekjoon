# 풀어본적 있는 문제지만 다시 풉니다. 그떄 못풀었거든요!
# 1:53
# 특정  프로세스가 몇번쨰로 실행되는지 알아내기.
# 문제가 조금 이해가 안가는데? 뭐지? 우선순위 값이 높을수록 좋은거임. 1이 1순위가 아님
# 그럼 이해가 된다. 그 뒤로는 실행된 프로세스의 우측으로 가면서 실행한다.
# 그럼 우선 가장 큰 값을 찾고, 그 뒤엔.. 슬라이싱 해서 붙이나? 
# priorities 는 값이 같은것도 있어서 프로세스라는 리스트를 새로 만들고, 
# 슬라이싱 똑같이 한 다음 .index+1 해서 반환할까.
# 우선순위가 같은게 있을수도 있는거아냐? 우선순위는 좌측부터인가..? 

# 인덱스로 값을 찾아야하는데 값이 겹쳐서 인덱스가 고정적이지 않아서 헷갈리네. 이걸 어쩐담...
# 그냥 sort 하고 아래 처럼 나올떄까지..음.. 그렇게 돌릴까?
'''
def solution(priorities, location):
    answer = 0 #정답
    n = len(priorities)
    process= [x for x in range(n)] # location 값을 찾기 위한 리스트?
    
    prios = sorted(priorities) # 비교용 정렬 프로세스
    
    for i in range(n):
        if priorities[i] != prios[i]: # 정렬이 안되어있어 그러면
            maxi_loc = priorities.index(max(priorities[i:])) # 첫번쨰로 실행될 프로세스의 위치를 찾되 정렬 안된 부분에서

            temp = priorities[:maxi_loc] # 실행된 프로세스의 좌측에 있는걸 우측으로 옮긴다- 실행순서를 바꾼다.
            priorities = priorities[maxi_loc:] + temp # 새롭게 붙인 리스트 
        
            temp = process[:maxi_loc] # location 으로 찾기 위한 리스트도 똑같이 순서를 섞어준다.
            process = process[maxi_loc:] + temp


    return answer
'''
# 결국 40분간 붙잡고 있다가 정답 봐버렸슴다
# 큐 를 사용하는게 중요하다. 
import queue

def solution(priorities, location):
    q = queue.Queue() # 큐 변수 선언
    index = queue.Queue() # 인덱스를 담을 큐 변수 선언
    l=sorted(priorities) # 정렬된 우선순위 배열을 반환, 저장

    for i,j in enumerate(priorities): #enumerate 메서드를 이용해서, 값과 인덱스값을 반환한다. 
        index.put(i) # 삽입
        q.put(j)    

    c=1 
    while q.qsize()>0: # q 라는 큐에 값이 없을때까지- 모두 실행할떄까지
        x, y = q.get(), index.get() # pop과 비슷하게 가장 앞에서부터 pop(0)
        if x==l[-1]: # 만약 그 값이 정렬된 값과 같다면
            l.pop() # l에서도 하나 빼고 
            if y==location: # 만약 인덱스가 로케이션(즉 정답이라면)
                return c # c값을 반환해서 몇번째인지 답을 알린다
            c+=1 # 아니면 순서가 뒤로 밀린거니 c 를 더한다
        else:
            q.put(x) #만약 아니라면 다시 후순위로 밀려난다. 다시 append 해준다
            index.put(y)
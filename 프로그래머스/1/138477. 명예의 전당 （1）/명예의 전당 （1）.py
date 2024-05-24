# 하루 한명씩 추가됨.
# 순위 상위 k 번째 이내이면 명예의 전당에 등록됨
# 매일 최하위 점수를 반환하시오

# 그냥 스택인데? 그냥 pop인데?

def solution(k, score):
    answer = []
    honor =[] # 현재 명예의 전당 상태
    temp = 0 #pop 이 담길 점수
    
    for i in score :
        if len(honor) < k : #만약 k 만큼 방영하지 않은경우
            honor.append(i) # 한번 넣는다. 
            honor.sort(reverse=True) #내림차순 정렬한다. 하나하나 비교하는것도 있지만 그냥 정렬하자.
            temp = honor[-1] # 마지막 인덱스가 최하점이니 넣는다
            answer.append(temp)
            
        
        else: # k 이상 방영해서 이제 경쟁하는경우
            if i > honor[-1] : # 만약 최하점보다 높은경우
                honor.pop() # 마지막 뺴고
                honor.append(i) 
                honor.sort(reverse=True)
                
                temp = honor[-1] # 마지막 인덱스가 최하점이니 넣는다
                answer.append(temp)
            else: # 최하점은 그대로인경우
                answer.append(temp)
            
    return answer
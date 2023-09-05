#논문 n 편 count 쓰기? 1000편이하...
#6,5,3,1,0 역순 정렬 시키고 요소별로 >= 한 갯수가 같으면... 거기서 중단
#이렇게 하면 시간 초과라 그럼 내림차순 정렬후  인덱스랑 요소랑 값 같은거 찾으면 되는거아님?

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    if citations[0] == 0: # 예외처리
        answer = 0
        return answer
        
    for i in range(len(citations)):
        if citations[i] >= (i+1):
            answer = i+1
    return answer

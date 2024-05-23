# 입력이 적어서 그냥 하나하나 while 로 계산해도 될듯



def solution(a, b, n):
    answer = 0
    while True :
        # n 을 내가 갖고있는 콜라병 수로 생각한다
        if n >= a : # 만약 갖고있는 콜라로 병을 받을 수 있으면
            n -=a 
            n += b # 병을  a 만큼 주고 b 만큼 받는다
            answer += b

        else :
            break
        
    return answer
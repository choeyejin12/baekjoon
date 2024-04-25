# 이번주 꽉차서 바쁘니까 힘내자 3시 30분 시작
# 초 단위의 주식가격이 담긴 배열 prices, 가격이 떨어지지 않은 기간은 몇초인지 retrun 하기?
# 음... 해당 가격이상으로 유지된 시간을 구하면 되는건가?
# 그리고 기준은 다음 초 부터구
# 마지막 가격은 무조건 0이겠다

# 총 길이가 10만이니까 그냥 하나씩 돌려도 시간상으론 괜찮을거같은데.. 그냥 구현으로 갈까?


def solution(prices):
    answer = [] # 정답
    n = len(prices)
    for i in range(n-1): # -1 해줘야함 마지막은 어차피 끝이니까
        # 떡락 안함
        time = n - i -1
        # 중간에 떨어지는 경우
        for j in range(i+1,n):
            if prices[j] < prices[i]:
                time = j - i
                break
        answer.append(time)
    answer.append(0) # 마지막은 무조건 0 
    
    return answer
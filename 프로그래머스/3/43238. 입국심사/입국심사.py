# 이분탐색 문제인걸 아니까 그냥 그렇게 푸는데.. 딱 이것만 봤을때 이분탐색이라는걸 어떻게 알까?
# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고싶다.
# 거기에 기다리는사람이 10억명.. 일단 기다리는 사람만 봐도 뭔가 효율적인 방법으로 행갸ㅔㅆ다는 생ㄱ가은 드네..
# 구해야되는 최종값은 시간이다. 그럼 좌우 도 시간. 최솟값은 1 최댓값은 times 중 가장 큰값 *n
def solution(n, times):

    # n명, times의 Len만큼의 심사관
    left = 1
    right = max(times) * n # 가장 큰값
    answer = right  # 최종적으로 최소 시간을 담을 변수
    
    # 이진 탐색 시작
    while left <= right:
        mid = (left + right) // 2  # 중간값
        
        people = 0
        for i in times:
            people += mid // i # 각 심사관이 mid 시간 동안 처리할 수 있는 사람 수
        
        # 만약 처리할 수 있는 사람 수가 n명 이상이면
        if people >= n:
            answer = mid  # 일단 가능하므로 답에 저장
            right = mid - 1  # 시간을 줄여서 더 최소 시간을 탐색
        else:
            left = mid + 1  # 처리할 수 있는 사람 수가 부족하면 시간을 늘림
    
    return answer
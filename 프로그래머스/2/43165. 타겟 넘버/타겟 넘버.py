# 나름 간단한편. 무난한 DFS 기본 문제

def solution(numbers, target):
    #DFS 부터 선언해줍시다
    def dfs(index, current_sum):
        # 모든 숫자를 다 사용한 경우
        if index == len(numbers):
            # 현재의 합이 목표값과 일치하면 1을 반환
            return 1 if current_sum == target else 0

        # 더할때
        add_case = dfs(index + 1, current_sum + numbers[index])

        # 현재 숫자를 뺼ㅉ떄
        subtract_case = dfs(index + 1, current_sum - numbers[index])

        # 더한 경우와 뺀 경우의 결과를 합산
        return add_case + subtract_case
    
    # DFS를 시작
    return dfs(0, 0)# 0에서 시작!!!!
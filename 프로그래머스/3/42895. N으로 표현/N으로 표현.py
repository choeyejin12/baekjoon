#사칙연산을 괄호 포함해서 하기... 아 쉽지않다
# 일단 숫자가 나오면 n을 nnnn이렇게 해서 사칙연산을 차근차근한다... 는 느김이겠찌?
# 각 단계의 숫자를 다 저장할건데 dp 리스트를 어떻게 만들지가 고민고민....
#아... 쉽징낳음 30분 보다가 포기하고 답보기

def solution(N, number):
    # N을 1회부터 8회까지 사용해서 만들 수 있는 숫자들을 저장할 리스트
    dp = [set() for _ in range(9)]
    
    # dp[i]는 N을 i번 사용해서 만들 수 있는 숫자들을 저장
    for i in range(1, 9):
        # N을 i번 반복해서 이어붙인 숫자를 추가 (예: N=5일 때 5, 55, 555 등)
        dp[i].add(int(str(N) * i))
    
    # 동적 프로그래밍으로 N을 i번 사용해서 만들 수 있는 모든 숫자를 구함
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:  # j번 사용해서 만든 숫자
                for op2 in dp[i - j]:  # i-j번 사용해서 만든 숫자
                    # 사칙연산을 통해 새로운 숫자를 dp[i]에 추가
                    dp[i].add(op1 + op2)  # 덧셈
                    dp[i].add(op1 - op2)  # 뺄셈
                    dp[i].add(op1 * op2)  # 곱셈
                    if op2 != 0:  # 나눗셈 (0으로 나누지 않도록 체크)
                        dp[i].add(op1 // op2)
        
        # 목표 숫자가 dp[i]에 있다면 i를 반환
        if number in dp[i]:
            return i
    
    # 8번 이하로 만들 수 없으면 -1 반환
    return -1

# 예시 실행
print(solution(5, 12))  # Output: 4
print(solution(2, 11))  # Output: 3

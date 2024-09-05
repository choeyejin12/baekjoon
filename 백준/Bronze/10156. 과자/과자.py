def calculate_shortage(K, N, M):
    total_cost = K * N
    if total_cost > M:
        return total_cost - M
    else:
        return 0

# 입력 받기
K, N, M = map(int, input().split())

# 결과 출력
print(calculate_shortage(K, N, M))
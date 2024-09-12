# 학생 점수를 리스트로 입력받습니다.
scores = []
for _ in range(5):
    score = int(input())
    # 점수가 40점 미만이면 40점으로 수정
    if score < 40:
        score = 40
    scores.append(score)

# 평균 계산
average_score = sum(scores) // 5

# 결과 출력
print(average_score)

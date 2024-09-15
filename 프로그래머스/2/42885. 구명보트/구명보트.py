# 일단 정렬부터 한 다음에.. 그리디니까 그냥 구명보트 개수 반환하는거고..
# 가벼운 사람 무거운사람 해서 채워나가면 될거같은데?

def solution(people, limit):
    people.sort()
    # 구명보트의 개수 정답
    boat = 0
    small_idx = 0
    big_idx = len(people) - 1 # 무거운사람이니까 하나 뺴
    
    # 가벼운사람부터 채우기
    while small_idx <= big_idx:
        if people[small_idx] + people[big_idx] <= limit:
            # 가벼운애 무거운애 태워..근데좀 코드가 살짝 길긴하다
            small_idx += 1
            big_idx -= 1
        else:
            # 무거운애만 태울수 있는 경우
            big_idx -= 1
            
        boat += 1
    
    return boat
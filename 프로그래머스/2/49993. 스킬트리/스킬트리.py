# 음. 구현 문제? 암튼 앞에 CBD 이게 있긴해야한다 이거자너
# 스킬 트리가 20 이하인 배열이고, 문자열도 26까지니까 수가 크지 않아서. 그냥 간단하게 가능할듯
# 그냥 원소 문자열 다 돌면서 앞의 값이 true 인지 보는 그런 간단한 코드면 될거같음
# len 값랑.. index 값이랑... 이렇게 저렇게?

def solution(skill, skill_trees):
    count = 0  #유효한 skill 순서를 갖춘 skill_trees의 개수를 세는 변수

    for tree in skill_trees:
        is_valid = True  # 지금 스킬 와도 되냐?
        index = 0  # 비교할 skill의 인덱스를 관리하는 변수

        for i in tree:
            if i in skill:
                # 3단이 맞나 싶긴한데 이게 편함...
                if i == skill[index]:
                    index += 1
                else:
                    is_valid = False
                    break

        if is_valid:
            count += 1

    return count

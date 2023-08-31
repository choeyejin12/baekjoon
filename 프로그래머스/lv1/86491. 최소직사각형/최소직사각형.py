#가로와 세로끼리중 가장 큰 값으로 가로 또는 세로를 정하고
#다음은 하나씩 돌려보면서... 해당 값에... 
#그냥 max 구한쪽으로 전부 방향 돌린셈 치고 두번째 에서 젤 큰수 구하면되는거아님?


def solution(sizes):
    hlist = []
    for i in range(len(sizes)):
        sizes[i].sort(reverse=True)
        hlist.append(sizes[i][1])
    width = max(sizes)
    width = width[0]
    hight = max(hlist)
    answer = width*hight
    return answer
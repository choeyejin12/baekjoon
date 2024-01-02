#음... 자료구조... 큐인가? 그렇기엔 중간에서 시작하니까....
#그리고 순위는 실시간으로 바뀌는거니 총 불린 횟수로 해서도 안되고... 콜링때마다 연산해주는게 좋을거같은데 콜링 길이도 그닥 길진않다.
#음...버블소트? 그런느낌으로? 해야하나?
#근데 더 간단하게 그냥 앞에랑 바꾸면 되는거 아님? 그 기초에 배우는 그 순서바꾸기 그걸로
#드가자
def solution(players, callings):

        #players[a-1], players[a] = players[a],players[a-1]#간단하게 스왑 을 하면 시간초과남
        #callings 가 그래도 길이가 길어서인듯
        #이땐 생각을 바꿔서 딕셔너리로 표현한다.
       # 선수들의 초기 순위를 인덱스로 매핑한 딕셔너리 생성
    # {"mumu" : 0, "soe" : 1, "poe" : 2, "kai" : 3, "mine" : 4}
    players_ranking = {player: int(idx) for idx, player in enumerate(players)}
#enumerate 나 itertools 같은 라이브러리 사용을 기억하자. 한번 더 정리해라
#그리고 컴프리헨션도 잘 알아두고
    for call in callings:
        current_rank = players_ranking[call]  # 호출된 선수의 현재 순위

        # {선수 : 순위} 딕셔너리에서 선수의 순위 바꿔주기
        players_ranking[call] -= 1
        players_ranking[players[current_rank - 1]] += 1

        # players 배열에서 선수들의 순위 바꿔주기
        players[current_rank - 1], players[current_rank] = call, players[current_rank - 1]

    answer = players
    #print(players)
    return players
#흠... 뭔가...애매하네 직관적으로 어떻게 풀지는 아직 안느껴져
#시작시간 09:26:31

# 조이스틱을 최소한으로 움직여서 영단어 만들기 - 음. 바로 직전 단어 기준에서 움직이는 거겠지
# 최소로 움직여서...그리디? 그냥 구현? 

# 그냥 위아래로 움직이는건 앞뒤로 움직이는거고, 양옆으로 움직이는건 맨 첫글자나 끝 글자가 되는거네.
# A Z 아니면 그냥 움직여서 넣는수밖에 없겠지? 어차피 무조건 순서대로 입력해야하니까.

# 음... 구현쪽으로 생각을 해 보자. 영단어 움직이는거를 인덱스로 한다 쳐서...

# 아니지. 뭔가 이분탐색 비슷한거 같은 느낌이 드는데? 이분탐색 같은데? 



# 결국 30분간 고민하다가 대가리 깨지고 답안 봤다!
'''
def solution(name):
    answer = 0
    alpab = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    alpab = list(alpab) # 인덱스로 움직? 이는... 조이스틱 암튼 구현
    
    count = 0 #조이스틱 움직이는 횟수
    # 이분탐색이 맞는거 같은데? 만약 내가 Y로 간다 치면은 26번 움직이는것 보다 옆으로 한번 위로 한번이 빠르잖아?
    # 아 이분탐색 다까먹었는데 골조 코드를 보면서 해보고 안되면 답을 보자
    
    # 아니 근데 그럼 같은글자를 여러번 입력할때는 뭐 어케해야하냐 이땐 안움직이는거같은데
    # 몰것다!!!!!!!!
    return answer
    
'''

def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer
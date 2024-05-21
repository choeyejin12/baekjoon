#그래...할수있어 하자 배고프지만 풀수있어 젠장
# 이 개판 자판을 이용해 문자열을 입력할 때, 키를 최소 몇번 눌러야 그 문자열을 작성하는지 알아보자

# keymap 의 인덱스만큼 키가 있는거고, 해당 인덱스 내부의 인덱스만큼 누를때마다 번호가 바뀐다
# 출력할 수 없는 키는 -1 을 하자.

# 출력은 또 targets 에 맞춰야한다. 키맵은 정말 키맵일 뿐이고 버튼을 누르는것은 키맵의 길이와는상관없이 최소로 할 수 있으면 된다.
# 기본적으로 inedx()를 쓰면 앞에서 부터 반환하니까.. 키맵별 인덱스를 보고 하는데...
# 일단 입력값이 적어서 뭘 쓰든 상관없을거같다. for문을 4번 돌려도 말이지...
# 살짝 DP 느낌으로가는것도 나쁘지않을거같은데 복잡하려나
# 이중리스트라 한 키씩 한 타겟씩 하는게 복잡하니까, 단어별로 리스트를 만들고 거기에 최소 출력 값을 넣어서
# 나오는 키마다 그렇게 하면 될듯

def solution(keymap, targets):
    answer = []
    #alpa = [0 for _ in range(26)] # 알파벳 수만큼의 리스트. 0은 A 임
    n = len(keymap)
    keymapall = (''.join(keymap))
    for i in targets :
        ans = 0
        
        for j in range(len(i)):
            key = i[j]
            knum = []
            print(key)
            for k in range(n):
                if key in keymap[k]:
                    a = keymap[k].index(key) +1
                    knum.append(a)
                
            
            if len(knum) == 0:
                ans = -1
                break
            else: 
                temp = min(knum)
                ans += temp
                    
        answer.append(ans)
                    
    return answer
#이름 배열 name, 그리움 점수 배열 yearing, 사진에 찍힌 인물의 이름을 담은"2차원" 배열 photo
#출력은 1차원 배열로, n = ren(photo)
#생각보다 간단하지않을까?
#index 메서드를 잘 쓰면 될거같은데
#name - yearning 세트고, photo 내의 배열만큼 반복문 돌리자


def solution(name, yearning, photo):
    answer = []
    n = len(photo)
    
    for i in range(n):
        score = 0
        
        for j in range(len(photo[i])):
            a = photo[i][j]
            print(a)
            
            if a in name:
                b = name.index(a)
                c = yearning[b]
                score +=c
                
            else:
                continue
                
        answer.append(score)

    print(answer)
                
    return answer
#이야 문제봐라.... 시작시각 08:05:54
#격자판. 여기서부터 약간 구현이나 그래프탐색... 하지만 레벨 1이니까 그래프탐색은 아니겠지
#간단히 절댓값으로 연산- 하는 그런느낌인거 같은데. 
#시작점과 끝점을 담은 정수 배열을 return 해라? 생각보다는 풀만하네

#그럼... 우선 입력받은 배경화면을 숫자좌표로 바꾸고.
#각 값들중에 가장 작은 값과 가장 큰값..인거겠지? 그런데 이제... 음... 가로 세로 고려해서 그냥 가장 큰 값들 좌표 반환하면되는거 아냐?

#입력값은 50이 최대이므로 브루트 포스로 숫자좌표로 변경 가능할듯

#숫자좌표로 변경 -> 가장 큰/작은 좌표값 출력 

#드가자~

def solution(wallpaper):
    answer = []
    h = len(wallpaper) # 배경화면의 세로값
    wallpaper = list(wallpaper)
    w = len(wallpaper[0]) # 배경화변 가로값
    
    start = [0,0] #시작 좌표 - 가장 작은 숫자들 저장
    end = [0,0] #끝 좌표 - 가장 큰 숫자들 저장
    hi = [] #세로 좌표들
    wi = [] #가로 좌표들
    #min, max 로... 세로랑 가로 따로 저장하고... min끼리 max 끼리 하면되는거 아님?
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == "#":
                hi.append(i)
                wi.append(j)
    
    print(hi)
    print(wi)

    answer= [min(hi),min(wi),max(hi)+1,max(wi)+1]
   
    print(answer)
    return answer
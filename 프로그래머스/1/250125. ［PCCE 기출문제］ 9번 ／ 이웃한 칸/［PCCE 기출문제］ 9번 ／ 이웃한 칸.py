#아.. 열심히 풀었는데 날라감...ㅠ
# 대략 15분정도 여까지 걸린듯.
# 친절하게 의사코드를 주니, 저 방식을 그대로 구현하는대로 가자. 

def solution(board, h, w):
    answer = 0
    n = len(board)
    count = 0
    print(n)
    
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    
    for i in range(4):
        print(i)
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n:
            print("h,w",h_check,w_check)
            if board[h][w] == board[h_check][w_check] :
                print(board[h_check][w_check])
                count +=1
            
    return count
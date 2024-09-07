import sys
# 서로 다른 n개의 자연수의 합이 S이다. S를 알 때, 자연수 N의 값은?
# 1+2+3+4+5+6+7 뭐 이런식으로..
# 그럼 2면 1+1은 안되니까 그냥 n은 1인가?
# 그럼.. 어차피 서로 다른 숫자여야 하니 주어진 S에서 1부터 빼가면서 하는게 맞다
# 1부터 시작하는 변수 k 보다 S-nK가 작을때.. 그때가 자연수 n의 최댓값이겠지
# 하지만 k 보다 남은수가 작으면 구현이 불가하니 그때도 뺀다.
# 43억 정도에 시간복잡도가 n 이니까.. 괜찮으려나
# while 문이 좀 불안하긴한데. 다른 스마트한 방법도 있긴할듯

#  아냐... 그리디라고 생각하면 k는 무조건 S보다는 작아야하는데?
# 그럼 소인수분해..아냐... 
# 그냥 S에서 1부터 커지는 K를 빼는게 맞지않아? 또 약간 DP? 도 될거같고
# 1부터 커지는 k를 빼는데? K + K+1 보다 S가 작으면? 안되는거지.
# 그럼 조건문이 조금 복잡해지긴 하겠지만 이게맞다
S = int(input())
n = 1 # 정답용 변수. 무조건 1부터 시작. 
k = 1 # n을 구하기 위해 1부터 시작하는 수

if S == 1 : # 예외처리
    print(n)
    sys.exit()
   

while True:
    if S == 0 : # 완전히 떨어지면 그냥 n 반환
        break
    if S < (k*2+1) : # 만약 다음에 올 숫자들 보다  커서, 불가하다면
       
        break
    else:
        S -= k
        n += 1
        k += 1
        
print(n)
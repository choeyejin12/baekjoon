#숫자카드 N개. 정수 M개.
#첫째줄 가진 N의 수, 둘째줄 N숫자카드, 셋째줄 M수, M 찾아야할 숫자
#답은 있으면 1 없으면 0 숫자카드의 순서에 따라서
#일단 in 함수를 이용해 찾아보자, 하지만 입력값이 커서 어려울수도 있다.
#in 함수를 이용한것은 시간이 오래 걸린다. 탐색중 시간이 가장 빠른 이분탐색 가보자.

n = int(input())
ncard = list(map(int,input().split()))
m = int(input())
mnum = list(map(int,input().split()))

ncard.sort() #이분 탐색을 위해 정렬

def binary  (num):
    l = 0 #인덱스 좌표는 0 부터 n-1 까지니까 그만큼을 주고. 
    r = n-1 #이분 탐색을 위한 위치기준 좌표들. 왼쪽 오른쪽이다.
    while l<= r :
        mid = (l+r)//2 #중간값. 이 값 기준으로 한다
        if ncard[mid] == num :
            return 1
        elif ncard[mid] > num : #중간값이 찾는값 보다 크면 왼쪽으로
            r = mid - 1 # 때문에 r 값을 이미 반띵한거에 또 반띵해서 이분탐색을 하는거다
        else :
            l = mid + 1 #만약 찾는값보다 작으면 오른쪽으로 중간값이 커져야 하니 왼쪽 범위를 반띵 이분탐색

    return 0 #만약 반띵탐색해서 못찾는다면, 없는거니 0

for i in range(m):
    num = mnum[i]
    print(binary(num), end =" ")
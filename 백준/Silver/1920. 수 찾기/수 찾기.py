'''
n = input()
n_list = list(map(int,input().split()))
m = input()
m_list = list(map(int,input().split()))

for i in m_list:
    if i in n_list :
        print(1)
    else :
        print(0)
'''
#in 을 사용해서도 간단하게 풀리지만 다른언어의 경우 안될수있음. 
#그러므로 이분탐색을 이용하자.
n = int(input())
num_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int,input().split()))
num_arr.sort()#이분탐색을 위해 정렬

def binary_search_rep(array,target,start,end):
    if start > end: #예외처리
        return 0 #NONE
    mid = (start+end)//2 #인덱스 중간지점

    if array[mid]==target:
        return 1 #mid
    elif array[mid]> target:
        return binary_search_rep(array,target,start,mid-1)
    else:
         return binary_search_rep(array,target,mid+1,end)

result = []
for i in m_arr :
    temp = binary_search_rep(num_arr,i,0,len(num_arr)-1)#함수호출하여 사용
    result.append(temp)

for _ in result:#출력을 맞추기 위해 for문으로 출력. 끝.
    print(_)
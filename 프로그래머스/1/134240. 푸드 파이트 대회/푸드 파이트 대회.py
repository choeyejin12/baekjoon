#1차원에서 양 끝에서 가운데로 빨리 오는 사람이 이긴다.좌우대칭.
#0번은 무조건 물. 1개다. 인덱스 순으로 칼로리가 높은 음식이다.
#이때 결과적으로 나올 음식의 배치는?

#음...2로 나누어서...//몫만큼만 넣고 또 반대로 넣으면 되는거같은데
#입력값이 크지 않으니 간단한 반복문으로 풀자.

def solution(food):
    answer = ''
    f = [1]#음식 들어갈 숫자리스트. 0은 물이고 항상 1이니 미리 넣어둔다.
    n= len(food)
    for i in range(1,n):
        a= food[i]//2 #2로 나눈 몫
        f.append(a) #몫만큼 0의 앞 뒤로 출력할 예정이니까.
    for j in range(1,len(f)):
        b=str(j)
        answer+=b*f[j]
    answer+="0"
    print(f)
    for k in reversed(range(1,len(f))):
        c =str(k)
        answer+=c*f[k]
    print(answer)
    return answer
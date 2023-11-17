#이런! 이건 과거의 내가 푼 적 있는 문제인걸!!!!
#헤헤 그래도 다시 풀어볼게
'''
def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer
    
'''
def solution(n, lost, reserve):
    answer = 0
    students, rent  = [1]*(n+1), [0]*(n+2)
    students[0],rent[0] = 3,3
    
    for lo in lost:
        students[lo] = 0
    for re in reserve:
        rent[re] = 1
        
    for i in range(1,n+1):
        if students[i] == 0:
            if rent[i] == 1: #본인이 여분을 가지고 있었을 경우
                rent[i] = 0 #도둑맞고 본인의 여분을 쓸경우 빌려줄 수 없기때문에 이 조건 먼저
                students[i] =1
            elif rent[i-1] == 1 and students[i-1] != 0: #뒤의 학생이 여분을 가지고 있었을 경우
                rent[i-1] = 0
                students[i] =1
            elif rent[i+1] == 1 and students[i+1] != 0:#앞의 학생이 여분을 가지고 있었을 경우 
                rent[i+1] = 0
                students[i] =1
                
    for student in students:
        if student == 1:
            answer += 1
    return answer

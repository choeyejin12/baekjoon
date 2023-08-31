def solution(answers):
    answer = []
    supo1=[1,2,3,4,5]
    supo2=[2,1,2,3,2,4,2,5]
    supo3=[3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    for i,v in enumerate(answers):#enumerate 사용법 익히자. i 는 인덱스 v는 벨류
        if v == supo1[ i %len(supo1)]:#이걸로 길이에 맞게 계산 :
            count[0]+=1
        if v == supo2[i%len(supo2)]:#이걸로 길이에 맞게 계산 :
            count[1]+=1
        if v == supo3[i%len(supo3)]:#이걸로 길이에 맞게 계산 
            count[2]+=1  
    for i,v in enumerate(count):
        if v == max(count):
            answer.append(i+1)
    print(answer)
    return answer
# 뒤에 있는 기능은 먼저개발 완료될 수 있지만, 앞의 기능이 개발 완료되어 배포될떄 함께 배포된다.
# 배포 순서대로 작업의 진도가 적인 정수배열 progresses , speeds 

# 각 배포마다 몇개의 기능이 배포되는지 반환?
# 총 길이는 100, 배포는 하루 한번, 하루끝에 이뤄지므로 95% 에 5% 면 1일 뒤 이뤄진다..? 당일 아니고?
# 1일 뒤가 맞는듯. 그럼 이제 앞의 기능이 완료되었을때 한번에 나오는게 몇개인지 알아야하는데..

# progress 랑 speed 해서 해당 기능의 완료일자만 넣은 배열 endday 을 새로 만들고, 그 배열에서 이케저케 하면 되는거 아님?
# 스택, 큐... 뭐... 리스트 쓰니까 스택인가? 스택이랑 큐를 꼭 서야하나?
# 그나마 큐 느낌일까.. 큐 구현이 가능하긴 하지만 일단 리스트 슬라이싱으로 그냥 하자

def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    # 우선 각 progress 들의 완료일을 담은 배열 endday 를 채우자
    endday = []
    
    for i in range(n):
        # 코드가 살짝 더럽긴한데 그래도... 
        tempx = (100-progresses[i])
        tempy = (tempx//speeds[i])
        if (tempx % speeds[i]) != 0 :
            # 만약 딱떨어지지 않는다면 +1일 해야하니까
            tempy +=1
        endday.append(tempy)
        
    print("endday",endday)
    # 위 코드를 통해 end day 는 모두 나옴. 이제 슬라이싱.. 을 하려면 for 문을 써야하는데 그게 안되는구나. 큐로 가자.아니면 while ?
    # 아냐 와일문 아니고 그냥 for 문 쓰는게 맞음
    
    for j in range(n):
        count = 1
        if len(endday)==1 :
            answer.append(count)
            break
        if not endday :
            break
        day = endday.pop(0) # 맨 처음 변수 pop
        
        
        print("day",day)
        
        for _ in range(n): # 이제 순회하면서 큰 값 있을떄까지 멈추고, count 추가
            if not endday :
                answer.append(count)
                break
            elif endday[0] <= day :
                count +=1
                print(count)
                endday.pop(0) # 이 부분이 잘 작동하는지 좀 걱정됨. 처리한 기능은 pop
            else:
                print("___",day,_)
                answer.append(count)
                break # 만약 k 가 day 보다 클 경우 순회 멈추기
    
        
    print(answer)
    return answer
# 12:25 시작 42분경 중단 1시부터 시작 
# 모든 트럭이 다리를 건너려면 최소 몇초?> 
# 다리에는 최대 bridge_length 만큼 올라갈수 있고, weight 만큼 무게를 견딜 수 있습니다.
# 다리 건너는데도 bridge_length 만큼 걸린다. 그럼... 
# 큐를 3개... 근데 이미 있는건 안해도 될거같고 다리 건너는 큐 하나, 지난 트럭..은 필요없구나. 그럼 음.. 어..
# 동시에 올라가는 그걸 구현해두면 그냥 1초 지날때마다 이케저케 하면 될듯? 

# 초가 지나는걸 기준으로 하자. 음. bridge_length 만큼 다리 건너는데 걸리는거니까...
'''
def solution(bridge_length, weight, truck_weights):
    answer = 1 # 1초부터 시작이니까... 이때 이미 트럭은 올라가 있다. 
    # 트럭은 대기트럭 순서대로다. 
    # 하나하나 셀 필요없이, 이미 있는 값이 weight 보다 적으면 1초 +
    # 커서 못들어가면 bridge_length answer 에 추가하고 하나 빼고 + 그럼 다리라는 리스트가 필요하겠구만
    
    t = truck_weights.pop(0) #
    bridge = [t] # 현재 다리 상태를 나타내는 변수.  첫번쨰 트럭 올리면서 시작.
    
    while True :
        print(bridge)   
        t = truck_weights[0] # 다음트럭 견적만
        
        if (sum(bridge)+t) <= weight : # 만약 올려도 괜찮다면 
            
            i = truck_weights.pop(0) # 다음 트럭 꺼내
            
            bridge.append(i) # 트럭 올려
            
            answer +=1 #트럭 올라가는 시간 추가 후.. 아 while 문으로 풀어야하나
            continue # 트럭 다리에 올린 후 다음 트럭 확인
            
        else : #만약 올릴 수 없다면
            bridge.pop(0) # 올라가 있는 트럭 하나 건너게하고
            
            answer +=(bridge_length-1) # 건넌 시간 추가해주기
            print("answer",answer)
            #print(bridge)
        
    

    return answer
'''
# 결국 또 50분동안 붙잡고도 못풀어서 답지를 봤습니다.. 난 빡대갈..ㅇ야...
# sum(iterable, start = 0)

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    second =0
    current_weight = 0
    while truck_weights :
        second +=1

        if bridge[0]!=0 :
            current_weight -= bridge[0]
        bridge.pop(0)
        bridge.append(0)
        incomming = truck_weights[0]

        if current_weight + incomming <= weight :
            bridge [-1] = truck_weights.pop(0)
            current_weight +=incomming

    return second + bridge_length
#입력값은 10만으로 그렇게 크지 않음.
#근데 적혀있는 카드가 값이커서 잘 되려나.원래는 그  수...
#만큼 배열을 만들고 인덱스값에 넣어서 찾으려했는데
#-범위가 있어서 그렇게는 안되겠고...
#그럼 결국 딕셔너리로 진짜 해야하나?

#딕셔너리는 value 와 key 값으로 이루어진 일종의...2차원배열?
#때문에 람다로.

n = int(input())#입력값
nums = {} #딕셔너리 선언
for _ in range(n):
    a = int(input()) #숫자
    if a in nums.keys():
        nums[a]+=1
    else:
        nums[a] =1

nums = sorted(nums.items(),key = lambda x:(-x[1],x[0]))#앞에 - 는 내림차순. 없으면 오름차순
print(nums[0][0])
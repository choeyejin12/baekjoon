#입력값은 3개로 정해져있다
a = int(input())
b = int(input())
c = int(input())
nums = ["0","1","2","3","4","5","6","7","8","9"]
n = str(a*b*c)
for _ in nums:
    num = n.count(_)
    print(num)
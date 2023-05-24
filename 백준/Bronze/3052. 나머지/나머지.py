nums = []
for _ in range(1,11):
    n = int(input())
    nums.append(n%42)
nums=list(set(nums))
print(len(nums))
#Сортирова вставками
nums = list(map(int, input().split()))

for i in range(0,len(nums)):
    for j in range(i+1, 1, -1):
        if nums[j] < nums[i]:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

print(nums)
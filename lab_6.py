#Сортирова выбором
nums = list(map(int, input().split()))


for i in range(len(nums)):

    min_n = 10**9
    min_i = i
    for j in range(i, len(nums)):
        if nums[j] < min_n:
            min_n = nums[j]
            min_i = j
    
    tmp = nums[i]
    nums[i] = min_n
    nums[min_i] = tmp

print(nums)
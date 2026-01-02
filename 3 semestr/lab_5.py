#Сортирова вставками
nums = list(map(int, input().split()))

for i in range(1,len(nums)):
    print(nums)
    j=i

    while nums[j-1] > nums[j] and j>0:
        tmp = nums[j-1]
        nums[j-1] = nums[j]
        nums[j] = tmp

        j-=1


print(nums)
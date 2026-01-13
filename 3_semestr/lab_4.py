#Сортирова методом прочесывания
nums = list(map(int, input().split()))

step = len(nums) - 1  


while step > 1:
    for i in range(int(len(nums)/step)):
        if nums[i] > nums[i+step]:
            tmp = nums[i]
            nums[i] = nums[i+step]
            nums[i+step] = tmp

        #print(nums, step)

    step = int(step /1.3)


for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp

print(nums)

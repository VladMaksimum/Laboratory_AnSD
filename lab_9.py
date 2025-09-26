#Сортирова поразрядовая
nums = list(map(int, input().split()))



for rep in range(len(nums)-2):
    #print('\n')
    #print(nums)
    #print(rep +1 , '======')
    for i in range(int((len(nums) - rep)/2) -1, -1, -1):
        j = i

        while not(2*j +1 > len(nums) - 2 - rep):
            #print('i was here', j, 2*j +1, len(nums) - 2 - rep)
            if nums[j] < nums[2*j + 1] or nums[j] < nums[2*j + 2]:
                if nums[2*j + 2] > nums[2*j + 1]:
                    tmp = nums[j]
                    nums[j] = nums[2*j + 2]
                    nums[2*j + 2] = tmp
                    j = 2*j + 2
                    continue
                else:
                    tmp = nums[j]
                    nums[j] = nums[2*j + 1]
                    nums[2*j + 1] = tmp
                    j = 2*j + 1
                    continue
            else:
                break
    

        
    #print(nums)
    
    tmp = nums[0]
    nums[0] = nums[len(nums)-rep-1]
    nums[len(nums)-rep-1] = tmp



if nums[0] > nums[1]:
    tmp = nums[0]
    nums[0] = nums[1]
    nums[1] = tmp

print(nums)

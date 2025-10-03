#Сортирова слиянием
nums = list(map(int, input().split()))



def merge_sort(nums: list):
    

    if len(nums) == 2:
        if nums[1] < nums[0]:
            return [nums[1], nums[0]]
        return [nums[1], nums[1]]
    
    if len(nums) == 1:
        return nums
    

    mass1 = merge_sort(nums[:(len(nums)//2):])
    mass2 = merge_sort(nums[(len(nums)//2)::])
    res=[]

    #print(mass1, mass2)



    i=0
    j=0

    while i< len(mass1) or j<len(mass2):
        if i< len(mass1) and j<len(mass2):
            if mass1[i] < mass2[j]:
                res.append(mass1[i])
                i+=1
            else:
                res.append(mass2[j])
                j+=1
        
        elif i< len(mass1):
            res.append(mass1[i])
            i+=1
        elif j<len(mass2):
            res.append(mass2[j])
            j+=1
    

    
    return res


print(merge_sort(nums))
        
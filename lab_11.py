#Сортирова быстрая
nums = list(map(int, input().split()))


def quick_sort(nums : list, start : int, end : int):
    #print("=============")


    #print(nums, start, end)
    if end-start <= 1:
        return

    i = start
    j = end

    

    pivot = nums[int((i+j)/2)]
    #print(pivot, int((i+j)/2))

    while i <= j:
        #print(nums[start:end+1], i, j)
        if nums[i] >= pivot and nums[j] <= pivot:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

            if nums[j] == pivot:
                i+=1
            elif nums[i] == pivot:
                j-=1
            else:
                j-=1
                i+=1

            continue

        if nums[i] < pivot:
            i+=1
        
        if nums[j] > pivot:
            j-=1

    
        
    #print(start, i)
    #print(j, end)

    if i-2<=end:
        quick_sort(nums, start, i-2)
    if j>= start:
        quick_sort(nums, j, end)


quick_sort(nums, 0, len(nums)-1)
print(nums)
        



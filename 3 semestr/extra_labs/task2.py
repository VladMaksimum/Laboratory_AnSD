
def quick_sort(nums : list, start : int, end : int, price: list):
    if end-start == 1:
        if nums[end] < nums[start]:
            tmp = nums[end]
            nums[end] = nums[start]
            nums[start] = tmp

        return
    
    if end - start <= 0:
        return

    i = start
    j = end


    pivot = nums[int((i+j)/2)]

    while i <= j:
        if nums[i] >= pivot and nums[j] <= pivot:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

            tmp = price[i]
            price[i] = price[j]
            price[j] = tmp

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

    if i-2<=end:
        quick_sort(nums, start, i-2, price)
    if j>= start:
        quick_sort(nums, j, end, price)


n, money = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
price = [int(i) for i in input().split()]

quick_sort(nums, 0, len(nums) - 1, price)

while len(nums) > 1:
    money -= price[0]

    if money <= 0:
        break
    else:
        price.pop(0)
        nums.pop(0)

print(nums[0])
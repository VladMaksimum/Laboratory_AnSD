#Сортирова поразрядовая
nums = list(map(int, input().split()))

ranks = [[] for _ in range(10)]


max_r = 0
max_num = max(nums)
while max_num !=0:
    max_r += 1
    max_num //= 10


for i in range(max_r):

    for elem in nums:
        ranks[ (elem%(10**(i+1)))//(10**i) ].append(elem)
    
    #print(ranks)
    nums.clear()
    for j in range(10):
        nums += ranks[j]
        ranks[j].clear()

print(nums)
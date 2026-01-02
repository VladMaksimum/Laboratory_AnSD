#Сортирова Шелла
nums = list(map(int, input().split()))

a = 3
k = 1/3

steps = []
n=1
while 2**n - 1 < len(nums):
    steps.insert(0, 2**n - 1)
    n+=1

#print(steps, len(nums))

for step in steps:
    for i in range(int(len(nums)/step)):
        ind_mass = [j for j in range(i, len(nums), step)]

        #print(ind_mass)

        #print([nums[i] for i in ind_mass])

        for k in range(1,len(ind_mass)):
            index=k

            while nums[ind_mass[index-1]] > nums[ind_mass[index]] and index>0:
                tmp = nums[ind_mass[index-1]]
                nums[ind_mass[index-1]] = nums[ind_mass[index]]
                nums[ind_mass[index]] = tmp

                index-=1
        
        #print([nums[i] for i in ind_mass])
        
print(nums)



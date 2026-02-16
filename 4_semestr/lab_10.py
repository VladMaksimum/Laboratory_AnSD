import random

def min_floor(floors):
    ans = 100
    # k(k+1)/2 >= N
    k = (-1 + (1 + 8 * floors) ** (1/2)) / 2
    if k % 1 != 0:
        k = int(k // 1 + 1)
    else:
        k = int(k // 1)

    move = 1
    last_floor = 1
    current = k
    
    broken = False
    while not broken:
        #print(current, k - move)
        if k < ans:
        #if random.choice([0,1]) == 0:
            last_floor = current
            if  current + k - move < floors:
                current += (k - move)
            else:
                current = floors
                break
        else:
            broken = True
        
        move += 1
    
    end = current
    start = last_floor
    #print(start, end)
    for i in range(start, end + 1):
        if i == ans:
        #if random.choice([0,1]) == 1:
            return i



floors = int(input())

print(min_floor(floors))


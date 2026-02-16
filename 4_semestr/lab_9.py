max_size = 2**31

def count_way(n, table):
    previous = [[-1 for _ in range(n)] for i in range(2**n)]
    costs = [[max_size for _ in range(n)] for i in range(2**n)]
    costs[1][0] = 0

    for mask in range(2**n):
        for i in range(n):
            if not(mask & (1 << i)):
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue
                
                #print(i, j, mask)

                if costs[mask | (1 << j)][j] > costs[mask][i] + table[i][j] and costs[mask][i] != max_size:
                    costs[mask | (1 << j)][j] = costs[mask][i] + table[i][j]
                    previous[mask | (1 << j)][j] = i
    
    min_cost = max_size
    current = 2**n - 1
    last_city = -1
    for i in range(len(costs[-1])):
        if min_cost > costs[-1][i]:
            min_cost = costs[-1][i]
            last_city = i
    
    way = []
    #print(previous, costs)
    while last_city != -1:
        way.append(last_city)
        #print(current, last_city)
        new_last_city = previous[current][last_city]
        if last_city != -1:
            current = current & ~(1 << last_city)
        
        last_city = new_last_city
        #print(last_city, way)
    
    return min_cost, way[::-1]
            


n = int(input())
table = []

for _ in range(n):
    table.append([int(i) for i in input().split()])

print(count_way(n, table))



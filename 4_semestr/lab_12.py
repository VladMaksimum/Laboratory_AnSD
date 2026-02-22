def fill_backpack(n: int, capacity: int, weights: list[int], cost: list[int]) -> int:
    v = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                v[i][w] = max(cost[i-1] + v[i-1][w - weights[i-1]], v[i-1][w])
    
    return v[n][capacity]


n = 4
capacity = 10
weights = [2, 3, 5, 7]
cost = [10, 15, 20, 25]

print(fill_backpack(n, capacity, weights, cost))



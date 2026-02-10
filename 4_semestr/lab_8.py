n = int(input())
coins = [int(i) for i in input().split()]
s = int(input())

dp = [0 for _ in range(s + 1)]
dp[0] = 1

for coin in coins:
    i = 0
    while i + coin < len(dp):
        dp[i + coin] += dp[i]
        i += 1
    
print(dp[-1])

n, k = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

count_list: list[list[int]] = [[] for _ in range(k)]

for number in nums:
    count_list[number % k].append(number)

cnt = len(count_list[0]) * (len(count_list[0]) - 1) / 2

for i in range(1, int((k-1)/2) + 1):
    cnt += len(count_list[i]) * len(count_list[k - i])

if k % 2 == 0:
    cnt += len(count_list[k//2])

print(int(cnt))
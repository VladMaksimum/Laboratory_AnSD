n = int(input())
arr = [int(i) for i in input().split()]

s = [0 for _ in range(n)] #част суммы
s[0] = arr[0]

if arr[0] < 0:
    cur_min = arr[0]
    min_ind = 0
else:
    cur_min = 0
    min_ind = -1

res = arr[0]
start = 0
end = 0


for i in range(1, n):
    s[i] = s[i-1] + arr[i]

    if res < s[i] - cur_min:
        res = s[i] - cur_min
        end = i
        start = min_ind + 1
    
    if s[i] < cur_min:
        cur_min = s[i]
        min_ind = i

print(res, start, end)


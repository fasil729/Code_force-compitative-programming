line = int(input())
col = [0] * line
row = []
for _ in range(line):
    arr = list(map(int, input().split()))
    row.append(sum(arr))
    for i in range(line):
        col[i] += arr[i]
res = 0
for r in row:
    for c in col:
        if c > r:
            res += 1
print(res)

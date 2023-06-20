n, m, k = map(int, input().split())

res = 0
arr = []
for _ in range(m + 1):
    arr.append(int(input()))
last = arr.pop()

for a in arr:
    if bin(a ^ last)[2:].count("1") <= k:
        res += 1
print(res) 
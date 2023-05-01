n, q = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * n
for _ in range(q):
    beg, end = map(int, input().split())
    prefix[beg - 1] += 1
    if end != n:
        prefix[end] -= 1

for j in range(1, len(prefix)):
    prefix[j] += prefix[j - 1]
prefix.sort(reverse=True)

arr.sort(reverse=True)
res = 0
for ind in range(len(prefix)):
    p = prefix[ind]
    a = arr[ind]
    res += p * a
print(res)




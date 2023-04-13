n, k = map(int, input().split())
res = float("-inf")
for i in range(n):
    f, t = map(int, input().split())
    res = max(res, min(f, f - (t - k)))
print(res)

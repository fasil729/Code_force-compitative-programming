n, m, k = map(int, input().split())
def f(num):
    tot = 0
    for i in range(1, n + 1):
        tot += min(num // i, m)
    return tot

l, r = 1, n * m

while l < r:
    mid = l + (r - l) // 2
    # print(mid, f(mid))
    if f(mid) < k:
        l = mid + 1
    else:
        r = mid
print(l)


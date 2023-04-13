from math import ceil
n, d = list(map(int, input().split()))
p = list(map(int, input().split()))
p.sort(reverse=True)
res = 0
ind = 0
for j in p:
    a = ceil((d + 1)/j)
    n -= a
    if n >= 0:
        res += 1
    else:
        break
print(res)



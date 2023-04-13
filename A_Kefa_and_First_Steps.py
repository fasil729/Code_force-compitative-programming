n = int(input())
a = list(map(int, input().split()))
temp = 1
res = 0
for ind, val in enumerate(a[:-1]):
    if a[ind] <= a[ind + 1]:
        temp += 1
    else:
        res = max(res, temp)
        temp = 1
res = max(res, temp)
print(res)

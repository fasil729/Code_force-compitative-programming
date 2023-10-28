import math


n, p = map(int, input().split())
arr = list(map(int, input().split()))

tot = sum(arr)
pref = [0]
for a in arr:
    pref.append(pref[-1] + a)
ans = [1, float("inf")]
for i in range(n):

    for j in range(n):
        if j >= i:
            diff = abs(j - i) + 1
            s = pref[j + 1] - pref[i]
        else:
            s = tot - (pref[i] - pref[j + 1])
            diff = n - (abs(j - i) - 1)
        # p -= s
        temp = diff + (n * math.ceil((p - s) / tot))
        if temp < ans[1]:
            ans = [i + 1, temp]
print(ans[0], ans[1])
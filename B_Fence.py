n, k = map(int, input().split())
a = list(map(int, input().split()))
pref_sum = [0]
for h in a:
    pref_sum.append(pref_sum[-1] + h)

ans = 1
mini = float("inf")
for ind in range(k, n + 1):
    tot = pref_sum[ind] - pref_sum[ind - k]
    if mini > tot:
        ans = ind - k + 1
        mini = min(mini, tot)
print(ans)

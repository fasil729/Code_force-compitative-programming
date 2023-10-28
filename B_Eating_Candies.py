t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pref = {}
    tot = 0
    for ind, num in enumerate(arr):
        tot += num
        pref[tot] = ind + 1
    tot = 0
    ans = 0
    for ind, num in enumerate(arr[::-1]):
        tot += num
        if tot in pref and pref[tot] + ind + 1 <= n:
            ans = max(ans, ind + 1 + pref[tot])
    print(ans)
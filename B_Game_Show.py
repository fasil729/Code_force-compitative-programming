k, n = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
coin = k
maxi = max(arr)

for i in range(2, int(maxi) + 1):
    count = 0
    coin = k
    for a in arr:
        if a % i == 0:
            count += 1
            continue
        if coin >= a:
            count += 1
            coin -= a
        else:
            break
    ans = max(ans, count)
if maxi == 1:
    print(min(k, n))
else:
    print(ans)
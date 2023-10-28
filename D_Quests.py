t = int(input())
for _ in range(t):
    n, c, d = map(int, input().split())
    q = list(map(int, input().split()))
    q.sort(reverse=True)
   

    def get_coins(k):
        ans = 0
        div, mod = divmod(d, k + 1)
        
        tot = sum(q[:k + 1])
        
        ans += div * tot
        ans += sum(q[:mod])
        return ans
    
    l, r = 0, d
    if get_coins(0) < c:
        print("Impossible")
        continue
    if get_coins(d + 1) >= c:
        print("Infinity")
        continue
    while l <= r:
        mid = l + ((r - l) // 2)
        if get_coins(mid) >= c:
            l = mid + 1
        else:
            r = mid - 1
    print(r)
    




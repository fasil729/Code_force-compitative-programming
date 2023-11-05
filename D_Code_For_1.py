n, l, r = map(int, input().split())

def get_code(ind, n):
    mid = n // 2
    if n == 0:
        return 0
    if ind == 0:
        return n % 2
    
    return get_code(ind % mid, mid)

ans = 0
for i in range(l - 1, r):
    n = 2 
    if get_code(i, n):
        ans += 1
print(ans)
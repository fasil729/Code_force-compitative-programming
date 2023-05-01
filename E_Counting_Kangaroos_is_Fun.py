n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
mid = (len(arr)) // 2 - 1
l, r = mid, len(arr) - 1
res = 0
while l >= 0:
    if arr[r] >= 2 * arr[l]:
        res += 1
        r -= 1
    
    l -= 1
# print(res)
# print(r, mid, l)

res = (n - res)
print(res)
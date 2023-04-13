n = int(input())
arr = list(map(int, input().split()))
left, right = 0, 0
ind, res = 0, 0
val = arr[ind]
while ind < len(arr) and arr[ind] == val:
    left += 1
    ind += 1
while ind < len(arr):
    
    val = arr[ind]
    right = 1
    ind += 1
    while ind < len(arr) and arr[ind] == val:
        right += 1
        ind += 1
    res = max(res, 2 * min(left, right))
    left = right
    

print(res)


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
leng = int(input())
for i in range(leng):
    num = int(input())
    low, high = 0, len(arr) - 1
    res = 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] <= num:
            res = mid + 1
            low = mid + 1
        else:
            high = mid - 1
        
    print(res) 

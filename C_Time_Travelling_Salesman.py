def get_max(arr, stock=None):
    ans = 0
    if not stock:
        stock = arr[0]
    i = 0
    while i < len(arr):
        if i == len(arr) - 1:
            if arr[i] > stock:
                ans += arr[i] - stock
            i += 1
            continue
        if arr[i] <= stock:
            stock = arr[i]
            i += 1
            continue
        maxi = arr[i]
        while i < len(arr)and arr[i] > arr[i - 1]:
            maxi = arr[i]
            i += 1
        ans += maxi - stock
        stock = arr[i]
       
    return ans
n = int(input())
arr = list(map(int, input().split()))


final = max(arr) - min(arr)
l, r = arr.index(min(arr)), arr.index(max(arr))

if l <= r:
    final += get_max(arr)
else:
    final += get_max(arr[r + 1:])


print(final)
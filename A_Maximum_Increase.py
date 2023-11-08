n = int(input())
arr = list(map(int, input().split()))
ans = 1
prev = arr[0]
temp = 1
for num in arr[1:]:
    if num > prev:
        temp += 1
    else:
        temp = 1
    ans = max(ans, temp)
    prev = num


print(ans)
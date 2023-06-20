n = int(input())
arr = list(map(int, input().split()))
visited = set()
res = 0

for i in range(len(arr)):
    if (i + 1) in visited or arr[i] in visited or arr[arr[i] - 1] in visited:
        continue
    visited.add(arr[i])
    visited.add(i + 1)
    visited.add(arr[arr[i] - 1])
    res += 1
print(res)
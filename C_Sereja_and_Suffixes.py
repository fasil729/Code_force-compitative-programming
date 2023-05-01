n , m = map(int, input().split())
arr = list(map(int, input().split()))
visited = set()
new_list = [0] * n
num = 0
for i in range(n - 1, -1, -1):
    if arr[i] not in visited:
        num += 1
        visited.add(arr[i])
    new_list[i] = num

for _ in range(m):
    ind = int(input()) - 1
    print(new_list[ind])
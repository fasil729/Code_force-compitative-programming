t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            maxi = max(arr[i - 1], maxi)
    print(maxi)


t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[1] + arr[2] >= 10:
        print("YES")
    else:
        print("NO")
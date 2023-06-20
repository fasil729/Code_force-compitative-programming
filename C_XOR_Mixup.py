t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    xor = 0
    for i in range(n):
        xor = 0
        for j in range(n):
            if i == j:
                continue
            xor ^= arr[j]
        if xor == arr[i]:
            print(xor)
            break
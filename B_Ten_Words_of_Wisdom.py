t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split()) 
        if a <= 10:
            arr.append((b, i + 1))
    arr.sort()
    print(arr[-1][1])
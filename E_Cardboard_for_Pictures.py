t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    a = 4 * n
    b = 0
    arr = list(map(int, input().split()))
    for num in arr:
        b += 4 * num
        c -= num ** 2
    w = (-b + (((b ** 2) + (4 * a * c)) ** 0.5)) / (2 * a)
    print(int(w))
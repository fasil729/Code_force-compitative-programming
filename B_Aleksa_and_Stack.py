t = int(input())
for _ in range(t):
    n = int(input())
    ans = [str(i) for i in range(6, n + 6)]
    print(" ".join(ans))
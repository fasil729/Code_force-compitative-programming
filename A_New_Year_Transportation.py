n, t = map(int, input().split())

a = list(map(int, input().split()))
i = 1
breaked = False
while i < n:
    i += a[i - 1]
    if i == t:
        print("YES")
        breaked = True
        break
if not breaked:
    print("NO")
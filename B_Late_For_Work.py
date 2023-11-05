t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    r = []
    gr = -1
    for i in range(n - 1, -1, -1):
        if s[i] == "g":
            gr = i
        r.append(gr)
    r = r[::-1]
    lef = -1
    ans = 0
    for j in range(n):
        if s[j] == "g":
            lef = j
            break
    
    for j in range(n):
        if s[j] == c:
            if r[j] != -1:
                ans = max(ans, r[j] - j)
            else:
                ans = max(ans, n - j + lef)
        
    print(ans)


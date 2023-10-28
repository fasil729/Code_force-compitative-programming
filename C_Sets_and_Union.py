t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(set(map(int, input().split()[1:])))
    s = set()
    for set2 in arr:
        s = s.union(set2)
    # print("main", s)
    u_leng = len(s)

    
    ans = 0

    for i in s:
        s = set()
        for set2 in arr:
            if i in set2:
                continue
            s = s.union(set2)
        ans = max(len(s), ans)
    print(ans)
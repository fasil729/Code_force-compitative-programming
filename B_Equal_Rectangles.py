test = int(input())
for _ in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    beg, end = 0, len(a) - 1
    area = a[beg] * a[end]
    breaked = False
    while beg <= end:
        if a[beg + 1] == a[beg] and a[end] == a[end - 1]:
            if a[beg] * a[end] == area:
                beg += 2
                end -= 2
            else:
                print("NO")
                breaked = True
                break
        else:
            print("NO")
            breaked = True
            break
        
    if not breaked:
        print("YES")

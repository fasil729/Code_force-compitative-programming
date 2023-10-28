t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = input()
    pref = [0]
    for num in a:
        pref.append(pref[-1] ^ num)
    x_0 = 0
    x_1 = 0
    for ind in range(n):
        if s[ind] == "0":
            x_0 ^= a[ind]
        else:
            x_1 ^= a[ind]
    
    q = int(input())
    ans = []
    for i in range(q):
        c = list(map(int, input().split()))
        
        if c[0] == 2:
            
            if c[1] == 0:
                ans.append(str(x_0))
            else:
                ans.append(str(x_1))
        else:
            l, r = c[1], c[2]
            net = pref[r] ^ pref[l - 1]
            x_0 ^= net
            x_1 ^= net
    print(" ".join(ans))
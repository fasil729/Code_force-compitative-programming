import math
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = 1
    tmp = 1
    ind = 1
    while ind < n:
        if s[ind] == s[ind - 1]:
            tmp += 1
        else:
            tmp = 1
        res = max(res, tmp)
        ind += 1
    print(res + 1)


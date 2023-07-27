t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    res = 1
    ind = 0
    for c in s[1:]:
        if c == s[ind] == "(":
            res += 1
        ind += 1
    print(res) 
t = int(input())

for _ in range(t):
    s = input()
    res = ""
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            i += 2
        else:
            res += s[i]
            i += 1
    if i == len(s) - 1:
        res += s[i]
    print("".join(sorted(set(res))))
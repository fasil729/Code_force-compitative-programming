t = int(input())

for _ in range(t):
    res = ""
    for i in range(8):
        s = input()
        for c in s:
            if c != ".":
                res += c
                break
    print(res)
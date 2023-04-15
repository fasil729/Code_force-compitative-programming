s = input().strip()
stack = []
res = 0
for c in s:
    if c == "(":
        stack.append(c)
    else:
        if not stack:
            continue
        res += 2
        stack.pop()
print(res)

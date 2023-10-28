s = input()
t = input()
s = s[::-1]
t = t[::-1]
n = max(len(s), len(t))
m = min(len(s), len(t))

leng = 0
for i in range(m):
    if s[i] == t[i]:
        leng += 1
    else:
        break
ans = (n - leng) + (m - leng)
print(ans)

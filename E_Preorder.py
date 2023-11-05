n = int(input())
s = input()
mod = 998244353
ans = 0
ind = 1
while ind < (2 ** n)  - 2:
    if s[ind] != s[ind + 1]:
        ans += 2
    ind += 2
print((2 ** ans) % mod)
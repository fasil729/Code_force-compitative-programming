f = input()
s = input()
res = ""
for i in range(len(f)):
    res += str(int(f[i]) ^ int(s[i]))
print(res)
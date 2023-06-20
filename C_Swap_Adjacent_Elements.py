n = input()
a = list(map(int, input().split()))
s = input()
k = 0
maxi = 0
for i in range(len(a) - 1):
    maxi = max(maxi, a[i])
    if s[i] == '0' and maxi != i + 1:
        k = 1
if(k):
    print("NO")
else:
    print("YES")
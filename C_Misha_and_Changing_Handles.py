n = int(input())
dic = {}
for _ in range(n):
    old, new = input().split()
    if old in dic:
        dic[new] = dic[old]
        del dic[old]
    else:
        dic[new] = old
print(len(dic))
for k, val in dic.items():
    print(val, k)
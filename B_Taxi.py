from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
count = Counter(arr)

res = 0
three = count[3]
two = count[2]
one = count[1]
res += count[4]
res += three
one -= min(three, one)
res += two // 2 + one // 4
if 2 * (two % 2) + (one % 4) > 4:

    res += 2 
elif (two % 2) + (one % 4) == 0:
    pass 
else:
    res += 1 
print(res)
from collections import defaultdict

n, m = map(int, input().split())
sorted_dict = defaultdict(int)
unsorted_dict = defaultdict(lambda: float('inf'))
for _ in range(m):
    t, l, r = map(int, input().split())
    if t:
        sorted_dict[l - 1] = max(sorted_dict[l-1], r)
    else:
        unsorted_dict[l - 1] = min(unsorted_dict[l-1], r)
arr = []
i = 0
val = 10
breaked = False
maxi = sorted_dict[i]
print(sorted_dict, unsorted_dict)
while i < n:
    print(maxi)
    if sorted_dict[i] and unsorted_dict[i] > maxi:
        size = sorted_dict[i] - i
        arr.extend([val - 1] * size)
        
        val -= 1
    elif unsorted_dict[i] <= maxi:
        breaked = True
        print("NO")
        break
        
    else:
        arr.append(val - 1)
    maxi = max(maxi, sorted_dict[i])
    i += 1
    
if not breaked:
    print("YES")
    print(arr)

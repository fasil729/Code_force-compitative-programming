from collections import defaultdict
q = int(input())
used = set()
handle = {}
for i in range(q):
    old, new = input().split()
    if new in used:
        continue
    used.add(new)
    if not old in handle:
        handle[new] = old
    else:
        handle[new] = handle[old]
        del handle[old]

print(len(handle))
for new, old in handle.items():
    if old and new:
        print(old, new)
    

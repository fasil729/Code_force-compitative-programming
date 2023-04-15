from collections import defaultdict

n = int(input())
tree = defaultdict(list)
for _ in range(n):
    line = input().split()
    tree[line[2].lower()].append(line[0].lower())


def max_depth(root):
    if not tree[root]:
        return 1
    res = 0
    for neigh in tree[root]:
        res = max(res, max_depth(neigh))
    return res + 1

print(max_depth("polycarp"))



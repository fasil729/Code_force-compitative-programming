from collections import defaultdict

n = int(input())
name_score = defaultdict(int)
inp = []
for _ in range(n):
    arr = input().split()
    l = len(arr) // 2
    for i in range(l):
        ind = 2 * i
        name, score = arr[ind], arr[ind + 1]
        score = int(score)
        inp.append([name, score])
        name_score[name] += score
maxi = 0
name_set = set()
for k, val in name_score.items():
    # print(k, val)

    maxi = max(maxi, val)

for k, val in name_score.items():
    if val == maxi:
        name_set.add(k)

name_score = defaultdict(int)
for name, score in inp:
    name_score[name] += score
    if name_score[name] >= maxi:
        if name in name_set:
            print(name)
            break



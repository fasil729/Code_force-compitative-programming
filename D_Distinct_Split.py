from collections import Counter


t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    count = Counter(s)
    tmp = len(count)
    res = tmp
    doubled = set()
    for char in s:
        if not char in doubled and count[char] > 1:
            tmp += 1
            doubled.add(char)
        elif char in doubled and count[char] == 1:
            tmp -= 1

        res = max(res, tmp)
        count[char] -= 1
         
    print(res)
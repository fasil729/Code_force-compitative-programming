t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    misplaced = set()
    placed = set()
    res = 0
    for ind, num in enumerate(arr):
        placed.add(num)
        if num in misplaced:
            misplaced.remove(num)
        if ind + 1 not in placed and num != ind + 1:
            misplaced.add(ind + 1)
        
        if not misplaced:
            res += 1

        
    print(res)
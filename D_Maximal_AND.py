def calculate_ans(n, k, arr):
    count = [0] * 31
    for a in arr:
        # print(bin(a))
        for i in range(31):
            if not (a & (1 << i)):
                 
                 count[i] += 1
    #     print(count)
    # print(count)
    res = 0
    for j in range(30, -1, -1):
        if count[j] <= k:
            res += (1 << j)
            k -= count[j]
    return res



t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(calculate_ans(n, k, arr))
    
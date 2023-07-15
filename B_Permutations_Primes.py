def solution():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 1:
            print(1)
            continue
        if n == 2:
            print(2, 1)
            continue
        ans = ["1"] * n
        ans[0] = str(2)
        val = 4
        for i in range(1, n):
            if i != n  // 2:
                ans[i] = (str(val))
                val += 1
        ans[n - 1] = str(3)
        print(" ".join(ans))
solution()
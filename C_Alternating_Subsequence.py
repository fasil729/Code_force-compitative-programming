def my_func():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        if len(arr) == 1:
            print(arr[0])
            continue
        maxi = arr[0]
        res = 0


        for i in range(1, n):
            if (-1 * arr[i] < 0 and -1 * arr[i - 1] < 0) or (- 1 * arr[i - 1] > 0 and -1 * arr[i] > 0):
                maxi = max(maxi, arr[i])
            else:
                res += maxi
                maxi = arr[i]
        res += maxi
        print(res)
my_func()


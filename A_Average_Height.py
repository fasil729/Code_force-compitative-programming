def my_func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        odd = []
        even = []
        for num in a:
            if num % 2 == 0:
                even.append(str(num))
            else:
                odd.append(str(num))
        res = even + odd
        print(" ".join(res))
my_func()
def divisor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    def my_func(l, r):
        for n in range(l, r + 1):
            d = divisor(n)
            if d != n:
                print(d, n - d)
                return
        
        print(-1)
    my_func(l, r)
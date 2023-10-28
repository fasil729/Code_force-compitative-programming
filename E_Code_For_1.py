def my_func():
    n, lef, r = map(int, input().split())
    if n == 0:
        print(0)
        return
    ones = []
    l = len(bin(n)) - 2
    while n >= 1:
        if n % 2:
            ones.append(l)
        l -= 1
        n //= 2
    res = 0
    for i in range(lef, r + 1):
        if i % 2:
            res += 1
            continue
        for o in ones:
            if (i - (2 ** (o - 1))) % (2 ** o) == 0:
                res += 1
                break

    print(res)
my_func()
    
    
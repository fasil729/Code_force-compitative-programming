def my_func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if sum(a) < a.count(1) + n or n == 1:
            print("NO")
        else:
            print("YES")
my_func()

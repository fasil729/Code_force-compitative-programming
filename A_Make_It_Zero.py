t = int(input())
for _ in range(t):
    n = int(input())
    arr = input()
    if n % 2 == 0:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(2, n)
        print(2, n)
        print(1, 2)
        print(1, 2)
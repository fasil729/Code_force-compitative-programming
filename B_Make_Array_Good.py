t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
   

    print(n)

    for i in range(n):
        print(i + 1, pow(2, (a[i]).bit_length()) - a[i])


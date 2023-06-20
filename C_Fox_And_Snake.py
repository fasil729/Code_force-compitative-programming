n, m = map(int, input().split())
ceil = ["#"] * m
reverse = ["."] * (m - 1) + ["#"]
ceil = "".join(ceil)
reverse = "".join(reverse)
turn = True

for i in range(n):
    if turn:
        print(ceil)
    else:
        print(reverse)
        reverse = reverse[::-1]
    turn = not turn


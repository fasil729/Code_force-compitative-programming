n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
p = p[1:]
q = q[1:]
steps = sorted(set(p + q))
arr = [i for i in range(1, n + 1)]
if steps == arr:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
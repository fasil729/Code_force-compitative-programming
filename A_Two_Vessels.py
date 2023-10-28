import math
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    diff = abs(b - a) / 2
    print(math.ceil(diff/c))
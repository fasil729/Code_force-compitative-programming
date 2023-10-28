import math
inp = list(map(int, input().split()))
n = inp[0] - 1
p1 = max(inp[1], inp[2])
p2 = min(inp[1], inp[2])

x = math.ceil((p1 * n) / (p1 + p2))

print(p2 + (x * p2))
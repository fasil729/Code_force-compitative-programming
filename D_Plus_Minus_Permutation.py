import math
t = int(input())
for _ in range(t):
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)
   
    n, x, y = map(int, input().split())
    lc = lcm(x, y)
    inter = n // (lc)
    x = n // x
    y = n // y

    x -= inter
    y -= inter
    left = ((y + 1) * y) // 2
    right = (((2 * n) - x + 1) * x) // 2
    print(right - left)
   
        

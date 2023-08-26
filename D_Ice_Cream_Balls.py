import math
def my_func():
    n = int(input())
    discriminant = 1 + (4 * 2 * n)
    res = math.ceil((1 + math.sqrt(discriminant)) / 2)
    print(res)
t = int(input())
for _ in range(t):
      my_func()
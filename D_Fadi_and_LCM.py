import math

def get_factors(number):
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i != number // i:
                factors.append(number // i)
    # factors.sort()
    return factors

n = int(input())
factors = get_factors(n)
m = len(factors)
i = (m) // 2
if n == 1:
    print(1, 1)
else:
    print(factors[-2], factors[-1])
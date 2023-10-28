t = int(input())
for _ in range(t):
    def calculate(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    n, k, a, b = map(int, input().split())
    cities = []
    for i in range(n):
        city = list(map(int, input().split()))
        cities.append(city)
    city_a = cities[a - 1]
    city_b = cities[b - 1]
    major_a = calculate(city_a, cities[0])
    major_b = calculate(city_b, cities[0])
    for i in range(k):
        major_a = min(major_a, calculate(city_a, cities[i]))
        major_b = min(major_b, calculate(city_b, cities[i]))
    print(min(calculate(city_a, city_b), major_a + major_b))

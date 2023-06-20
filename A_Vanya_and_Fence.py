n, h = map(int, input().split())

a = list(map(int, input().split()))

width = 0

for a_i in a:
    if a_i > h:
        width += 1
    width += 1
print(width)
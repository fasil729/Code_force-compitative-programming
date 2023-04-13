n, k = map(int, input().split())
hr = 4 * 60 - k
count = 0
for i in range(1, n + 1):
    hr -= i * 5
    if hr >= 0:
        count += 1
    else:
        break
print(count)


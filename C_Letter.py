s = input()
lower = []
upper = []
count = 0
for char in s:
    if char.islower():
        count += 1
    upper.append(count)

count = 0
for char in s[::-1]:
    if char.isupper():
        count += 1
    lower.append(count)  

lower = lower[::-1]

n = len(s)
ans = min(lower[0], upper[-1])
for i in range(len(s) - 1):
    ans = min(ans, upper[i] + lower[i + 1])

print(ans)
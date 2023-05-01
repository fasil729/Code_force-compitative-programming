n, t = map(int, input().split())
listed = []
for char in input():
    listed.append(char)

for _ in range(t):
    i = 0
    while i < len(listed) - 1:
        if listed[i + 1] == "G" and listed[i] == "B":
            listed[i], listed[i + 1] = listed[i + 1], listed[i]
            i += 2
        else:
            i += 1
print("".join(listed))
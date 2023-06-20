row = [1, 2, 3, 4, 5, 6, 7, 8]
col = ["a", "b", "c", "d", "e", "f", "g", "h"]
s = input()
s_x, s_y = s[0], int(s[1])
t = input()
t_x, t_y = t[0], int(t[1])

x = abs(col.index(s_x) - col.index(t_x))
y = abs(t_y - s_y)
n = max(x, y)

if s_y > t_y:
    move_y = "D"
else:
    move_y = "U"

if s_x > t_x:
    move_x = "L"
else:
    move_x = "R"

print(n)
for i in range(n):
    if i < min(x, y):
        print(move_x + move_y)
    else:
        if x > y:
            print(move_x)
        else:
            print(move_y)


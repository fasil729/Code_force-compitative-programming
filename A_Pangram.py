n = int(input())
s = input()

s = s.lower()
set_s = set(s)
if len(set_s) == 26:
    print("YES")
else:
    print("NO")
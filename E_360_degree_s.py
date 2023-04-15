
def recurse(ind, res):
    global n
    if ind == n and res == 0:
        return True
    if ind == n:
        return False 
    return recurse(ind + 1, (res + deg[ind]) % 360) or recurse(ind + 1, (res - deg[ind]) % 360)
    

n = int(input())
deg = []
for _ in range(n):
    deg.append(int(input()))
if recurse(0, 0):
    print("YES")
else:
    print("NO")






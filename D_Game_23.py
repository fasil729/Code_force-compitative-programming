n, m = map(int, input().split())

def game(n, m):
    if n > m:
        return None
    if n == m:
        return 0
    b_2 = game(n * 2, m)
    if b_2 != None:
        return 1 + b_2 
    b_3 = game(n * 3, m)
    if b_3 != None:
        return 1 + b_3
    return None
res = game(n, m)
if res != None:
    print(res)
else:
    print(-1)

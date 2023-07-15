from collections import defaultdict

def my_func():
    n = int(input())
    q = list(map(int, input().split()))
    root = q.index(max(q)) + 1

    m = int(input())
    cost_dict = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        if not cost_dict[b]:
            cost_dict[b] = (c, a)
        else:
            cost_dict[b] = min(cost_dict[b], (c, a))
    if len(cost_dict) < n - 1:
        print(-1)
        return
    cost = 0
    for node in cost_dict:
        cost += cost_dict[node][0]


    print(cost)
    return

my_func()


        

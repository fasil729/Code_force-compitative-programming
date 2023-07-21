def my_func():
    
    n, m, k = map(int, input().split())
    x , y = map(int, input().split())
    ans = "YES"
    
    for i in range(k):
        x_i, y_i = map(int, input().split())
        if ((x_i + y_i) % 2) == ((x + y) % 2):
            ans = "NO"
    return ans

t  = int(input())

for _ in range(t):
    print(my_func())
        
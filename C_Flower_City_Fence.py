def my_func():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        val = arr[i]
        if val > n or arr[val - 1] < i + 1:
             print("NO")
             return
        
    print("YES")
t = int(input())
for _ in range(t):
      my_func()
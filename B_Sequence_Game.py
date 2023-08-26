def my_func():
    n = int(input())
    arr = list(map(int, input().split()))
    res = [str(arr[0])]
    for i in range(1, n):
        if int(res[-1]) > arr[i]:
             res.append(str(arr[i]))
        res.append(str(arr[i]))
    print(len(res))
    print(" ".join(res))
t = int(input())
for _ in range(t):
      my_func()
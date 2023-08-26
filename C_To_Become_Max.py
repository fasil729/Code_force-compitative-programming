t = int(input())
for _ in range(t):
    def my_func():
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        arr = arr[::-1]
        maxi = max(arr)
        for i in range(0, n - 1):
            t = k
            temp = arr[i]
            for j in range(i + 1, n):
                if temp >= arr[j]:
                    temp += 1
                    t -= (temp - arr[j])
                    if t >= 0:
                        maxi = max(maxi, temp)
                    else:
                        break
                else:
                    break
        print(maxi)
    my_func()

            

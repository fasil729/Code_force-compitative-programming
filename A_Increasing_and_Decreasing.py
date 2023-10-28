def my_func():
    x, y, n = map(int, input().split())
    res = [str(y)]
    if n == 2:
        print(x, y)
        return
    
    num = x + 1
    for num in range(x + 1, y):
        diff = x
        res.append(str(num))
        while num >= x:
            if len(res) == n:
                
                print(" ".join(res[::-1]))
                return
               
    
            diff = int(res[-2]) - int(res[-1])
            
            
            num = num - diff - 1
            if len(res) == n - 1 and num >= x:
                    res.append(str(x))
                    continue
            if num > x:
                
                res.append(str(num))
            else:
                res = [str(y)]
                break
    print(-1)


    
    


t = int(input())
for _ in range(t):
    my_func()
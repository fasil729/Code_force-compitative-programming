def func():
    n = int(input())
    arr = list(map(int, input().split()))
    ind = 1
    while ind < n and arr[ind] > arr[ind - 1]:
        ind += 1
    if ind == n:
        print("yes")
        print(1, 1)
        return
    start = ind - 1
    while ind < n and arr[ind] < arr[ind - 1]:
        ind += 1
    end = ind - 1
    # print(end, arr[start - 1])
    if ind < n and (arr[start] > arr[ind]) or start > 0 and arr[end] < arr[start - 1]:
        print("no")
        return
    
    while ind < n and arr[ind] > arr[ind - 1]:
        ind += 1
    if ind == n:
        print("yes")
        print(start + 1, end + 1)
        return 
    else:
        
        print("no")
func()
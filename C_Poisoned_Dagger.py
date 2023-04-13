test = int(input())
for i in range(test):
    leng, h = map(int, input().split())
    listed = list(map(int, input().split()))
    def is_k(list, k):
        count = 0
        for j in range(len(list) - 1):
            diff = list[j + 1] - list[j]
            if  diff >= k:
                count += k 
            else:
                count += diff
        count += k 
        return count >= h
    low = 1
    high = h
    while low <= high:
        mid = low + (high - low) // 2
        if is_k(listed, mid):
            high = mid - 1
        else:
            low = mid + 1
    print(low)

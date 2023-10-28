t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    b = len(bin(max(arr))) - 2
    prefix = [[0] * b]

    # Calculate prefix bitwise AND result
    for num in arr:
        prev = prefix[-1][0:]
        bini = bin(num)[2:]
        bini = "0" * (b - len(bini)) + bini 
        for ind in range(b):
             prev[ind] += int(bini[ind])
        prefix.append(prev)
    # print(prefix)
    def get_bitwise_and(left_index, right_index):
        num = ""
        for i in range(b):
            if prefix[right_index][i] - prefix[left_index - 1][i] == right_index - left_index + 1:
                num += "1"
            else:
                num += "0"
        
        return int(num, 2)
    
    def binary_search(l, r, k):
        left = l
        while l < r + 1:
            mid = (l + r) // 2
            if get_bitwise_and(left, mid) >= k:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1

    q = int(input())
    ans = []
    for i in range(q):
        l, k = map(int, input().split())
        if get_bitwise_and(l, l) < k:
            ans.append("-1")
        else:
            ans.append(str(binary_search(l, n, k)))

    print(" ".join(ans))
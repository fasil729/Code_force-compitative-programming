from collections import Counter


q = int(input())

for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = [0] * n
    for t in arr:
        freq[t - 1] += 1
    freq.sort(reverse=True)
    res = freq[0]
    ind = 0
    for val in freq[1:]:
        ind += 1
        if freq[ind - 1] < 1:
            break
        elif val >= freq[ind - 1]:
            res += freq[ind - 1] - 1
            freq[ind] = freq[ind - 1] - 1

            

        else:
            res += val
            
    print(res)

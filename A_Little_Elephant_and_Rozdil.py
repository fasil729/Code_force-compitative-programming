n = int(input())

arr = list(map(int, input().split()))
mini = min(arr)
ind = arr.index(mini)

if arr.count(mini) == 1:
    print(ind + 1)
else:
    print("Still Rozdil")
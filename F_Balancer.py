n = int(input())
arr = list(map(int, input().split()))
average = sum(arr) // n
move = 0

for ind in range(n - 1):
    diff = arr[ind] - average
    arr[ind + 1] += diff
    move += abs(diff)
print(int(move))
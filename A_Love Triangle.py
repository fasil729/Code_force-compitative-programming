from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))

def my_func():
    for ind, a in enumerate(arr):
        if arr[arr[a - 1]] == ind + 1:
            print(True)
            return
    print(False)

my_func()

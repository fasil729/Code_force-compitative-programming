n = int(input())
arr = list(map(int, input().split()))

siraja, dima = 0, 0
Turn = True

while arr:
    if arr[0] > arr[-1]:
        val = arr.pop(0)
    else:
        val = arr.pop()
    if Turn:
        siraja += val
    else:
        dima += val
    Turn = not Turn
print(siraja, dima)


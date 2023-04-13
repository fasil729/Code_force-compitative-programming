test = int(input())
for i in range(test):
    inp = list(map(int, input().split()))
    if inp[1] != 0:
        listed = list(map(int, input().split()))
    else:
        listed = []
    listed.sort(reverse=True)
    student = inp[0]
    count = 0
    outlet = 2
    for i in listed:
        if outlet >= student:
            break
        else:
            outlet += i - 1
            count += 1
    if outlet < student:
        print(-1)
    else:
        print(count)
    
test = int(input())
stack = []
x = 0
for _ in range(test):
    line = input().split()
    if len(line) == 2:
        stack.append([int(line[1]), 0])
    else:
        if line[0] == "add":
            if stack:
                stack[-1][1] += 1
            else:
                x += 1
        else:
            n, val = stack.pop()
            if stack:
                stack[-1][1] += n * val
            else:
                x += n * val
if x < 2**32:
    print(x)
else:
    print("OVERFLOW!!!")


        
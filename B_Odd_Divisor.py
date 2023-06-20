test = int(input())

for _ in range(test):
    if bin(int(input())).count("1") == 1:
        print("NO")
    else:
        print("YES")
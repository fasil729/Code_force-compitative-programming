n = int(input())
a = list(map(int, input().split()))
a.sort()

print(" ".join(str(j) for j in  a))
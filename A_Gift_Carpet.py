def my_func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        arr = [set() for i in range(m)]
        for i in range(n):
            for j, char in enumerate(input()):
                arr[j].add(char)
        name = ["v", "i", "k", "a"]
        ind = 0
        breaked = False
        for i in range(m):
            if name[ind] in arr[i]:
                ind += 1
            if ind == 4:
                print("YES")
                breaked = True
                break
        if not breaked:
            print("NO")
my_func()

def my_func():
    n = input()
    count = 0

    for d in n:
        if d == "7" or d == "4":
            count += 1
    for d in str(count):
        if d != "7" and d != "4":
            print("NO")
            return
    print("YES")
my_func()

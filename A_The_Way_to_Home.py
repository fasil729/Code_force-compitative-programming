
def main():
    n, d = map(int, input().split())
    s = input()
    ind = 0
    res = 0
    while ind < n - 1:
        start = ind
        ind += d
        while ind < n and s[ind] == "0":
            ind -= 1
            if ind == start:
                return -1
       
        
        res += 1
    return res
print(main())


   


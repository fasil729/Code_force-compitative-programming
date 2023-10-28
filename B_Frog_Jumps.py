t = int(input())
for _ in range(t):
    s = input()
    maxi = 0
    temp = 0
    i = 0
    while i < len(s):        
        if s[i] == "L":
            temp += 1
        else: 
            temp = 0
        maxi = max(maxi, temp + 1)
        i += 1
    print(maxi)
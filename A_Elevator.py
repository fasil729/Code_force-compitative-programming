leng = int(input())
for i in range(leng):
    inp = list(map(int, input().split()))
    if inp[0] <= inp[1]:
        print(inp[0] * 4)
    else:
        lift = (inp[2] * inp[1]) + (4 * inp[1]) 
        foot = (inp[0] * inp[2]) + (inp[1] * (4 - inp[2]))
        if lift > foot:
            print(foot) 
        else:
            print(lift)        
# inp = list(map(int, input().split()))
# list = list(map(int, input().split()))
# list.sort()
# n, min, max = inp[0], inp[1], inp[2]
# def sub(list):
#     global min
#     global max
#     beg, count = 0, 0
#     sum = 0
#     for i in range(len(list)):
#         if sum < min:
#             sum += list[i]
       
#         if sum > max:
#             sum -= list[beg]
#             beg += 1
#         if min <= sum <= max:
#             count += 1
#             sum = 0
#             beg = i + 1
#     return count
# print(sub(list))   

n, a, b = map(int, input().split())
x = list(map(int, input().split()))

j1 = s1 = j2 = s2 = res = 0
for i in range(n):
    
    while j1 < n and s1 + x[j1] < a:
        s1 += x[j1]
        j1 += 1
        
    while j2 < n and s2 + x[j2] <= b:
        s2 += x[j2]
        j2 += 1
        
    res += j2 - j1 
    s1 -= x[i]
    s2 -= x[i]

print(res)
           
       
 

# low, high = 1, len(list)

# while low <= high:
#     mid = low + (high - low) // 2
#     if sub()
        


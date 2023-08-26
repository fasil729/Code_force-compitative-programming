def is_yasser_happy(t, test_cases):
    for _ in range(t):
        n = test_cases[_][0]
        a = test_cases[_][1]
        prefix_sum = [0] * (n + 1)
        suffix_sum = [0] * (n + 1)
        
        # Calculate prefix sum
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
        
        # Calculate suffix sum
        for i in range(n, 0, -1):
            suffix_sum[i] = suffix_sum[i + 1] + a[i - 1]
        
        yasser_sum = prefix_sum[n]
        adel_sum = float("-inf")
        
        # Find the maximum segment sum that Adel can choose
        for i in range(1, n):
            adel_sum = max(adel_sum, suffix_sum[i + 1])
        
        if yasser_sum > adel_sum:
            print("YES")
        else:
            print("NO")

# Read input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Call the function
is_yasser_happy(t, test_cases)


# def my_func():
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         a = list(map(int, input().split()))
#         res = 0 
#         maxi = float("-inf")
#         boo = True
#         for ind, num in enumerate(a):
#             res += num
#             maxi = max(res, maxi)
#             if num <= 0:
#                 boo = False
            
#             if res < 0:
#                 res = 0
#         if maxi == sum(a) and boo:
#             print("YES")
#         elif maxi < sum(a):
#             print("YES")
#         else:
#             print("NO")
# my_func()
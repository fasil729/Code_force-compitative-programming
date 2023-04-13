# def inp():
#     return(int(input()))
# def inlt():
#     return(list(map(int,input().split())))
# def insr():
#     s = input()
#     return(list(s[:len(s)-1]))
# def invr():
#     return(map(int,input().split()))
 
# import sys
# # sys.setrecursionlimit(200000)
# import math
# from collections import Counter
# from collections import defaultdict
# from collections import deque
# input = sys.stdin.readline
# from functools import lru_cache
# import heapq 
# import threading
# ############ ---- Input Functions ---- ############
# def inp():
#     return(int(input()))
# def inlt():
#     return(list(map(int,input().split())))
# def insr():
#     s = input()
#     return(list(s[:len(s)-1]))
# def invr():
#     return(map(int,input().split()))
 
# cases = inp()
# for case in range(cases):
#     n = inp()
#     arr = insr()
#     total = 0
#     count = 0
#     dic = defaultdict(int)
#     dic[0] = 1
#     for r in range(len(arr)):
#         total += int(arr[r])
#         count += dic[total - (r+1)]
#         dic[total - (r+1)] += 1
    
#     print(count)










from collections import defaultdict


tests = int(input())
for test in range(tests):
    n = int(input())
    arr = input()
    pref_sum = []
    tot = 0
    dic = defaultdict(int)
    dic[0] = 1
    res = 0
    for j, val in enumerate(arr):
        tot += int(val)
        key = tot - (j + 1)
        res += dic[key]
        dic[key] += 1
    print(res)
    # res = 0
    
    # dic[0] = 1
    # for p in pref_sum:
    #     if p in dic:
    #         res += dic[p]
    #         dic[p] += 1
    #     else:
    #         dic[p] = 1
    # print(res)
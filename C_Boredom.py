from collections import Counter
from functools import lru_cache
import sys
import threading

def main():
    n = int(input())
    a = list(map(int, input().split()))

    count = Counter(a)
    maxi = max(a)

    @lru_cache
    def dp(num):
        if num > maxi:
            return 0
        freq = 0
        if num in count:
            freq = count[num]
        return max(freq * num + dp(num + 2), dp(num + 1))

    print(dp(1))

threading.stack_size(1 << 27)
sys.setrecursionlimit(1 << 30)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
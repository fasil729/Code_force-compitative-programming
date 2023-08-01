def my_func():
    from functools import lru_cache
    s = input()
    n = len(s)
    
    @lru_cache
    def dp(index, num):
        if num and int(num) % 8 == 0:
            print("YES")
            print(int(num))
            
            return True
        if len(num) == 3:
            return False
        
        if index >= n:
            return False
        
        return dp(index + 1, num + s[index]) or dp(index + 1, num)

    if not dp(0, ""):
        print("NO")
my_func()
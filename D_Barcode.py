import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, m, x, y = map(int, input().split())
    arr = [0] * m
    for _ in range(n):
        s = input()
        for i in range(len(s)):
            if s[i] == ".":
                arr[i] += 1
    print(arr)
    
    def dp(index, Is_dot, tot, res):
        if tot > y:
             return False, 0
        
        if index >= m:
            if not (x <= tot <= y):
                return False, 0
            return True, res
        
        if Is_dot:
            i = arr[index]
            j = m - arr[index]
        else:
            j = arr[index]
            i = m - arr[index]
        
        res_1 = dp(index + 1, not Is_dot, tot + 1, res + j)
        res_2 = dp(index + 1, Is_dot, tot, res + i)
        print(res_1, res_2, tot)
        if res_1[0] and res_2[0]:
            return True, min(res_1[1], res_2[1])
        elif res_1[0]:
            return True, res_1[1]
        elif res_2[0]:
            return True, res_2[1]
        return False, 0
    res_1 = dp(0, True, 0, 0)
    res_2 = dp(0, False, 0, 0) 
    if res_1[0] and res_2[0]:
            print(min(res_1[1], res_2[1]))
    elif res_1[0]:
            print(res_1[1])
    elif res_2[0]:
            print(res_2[1]) 
    

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
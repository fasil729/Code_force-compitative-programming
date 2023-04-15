from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your code here
    def recurse(root):
        white = 0
        black = 0
        res = 0
        if color[root] == "W":
            white = 1
        else:
            black = 1
        
        if not tree[root]:
            return 0, white, black
        
        
        for neigh in tree[root]:
            r, w, b = recurse(neigh)
            res += r
            white += w
            black += b
        if white == black:
            res += 1
        return res, white, black
    

    test = int(input())
    for _ in range(test):
        tree = defaultdict(list)
        n = int(input())
        a = list(map(int, input().split()))
        s = input().strip()
        color = {}
        ind = 2
        for i in a:
            tree[i].append(ind)
            ind += 1
        
        i = 1
        for co in s:
            color[i] = co
            i += 1
        print(recurse(1)[0])

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


    




import sys, threading


def main():
    test = int(input())
    ind = 1
    tree = {}
    for i in range(test):
        val = int(input())
        if val in tree and val != -1:
            tree[val].append(ind)
        elif val != -1:
            tree[val] = [ind]
        ind += 1
    class c:

        def max_Depth(self, root, visited, tree):
            if root in visited:
                return visited[root]
            if root not in tree:
                return 1
            dep = 0
            for j in tree[root]:
                visited[j] = self.max_Depth(j, visited, tree)
                dep = max(dep, visited[j])
            return dep + 1
        
    ob = c()
    res = 1
    visited = {}
    for key in tree:
        if key in visited:
            res = max(res, visited[key])
        else:
            visited[key] = ob.max_Depth(key, visited, tree)
            res = max(res, visited[key])
    print(res)
    

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 16)
    threading.stack_size(1 << 16)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
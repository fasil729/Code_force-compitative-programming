from collections import defaultdict
import sys, threading
def main():
    test = int(input())
    for i in range(test):
        leng = int(input())
        listed = list(map(int, input().split()))
        tree = defaultdict(list)
        length = 1
        root = None
        for ind, node in enumerate(listed):
            if node == ind + 1:
                root = node
            else:
                tree[node].append(ind + 1)
                if len(tree[node]) > 1:
                    length += 1

        print(length)

        def vertical_path(root, path):
            path.append(str(root))
            if not tree[root]:
                print(len(path))
                print(" ".join(path))
            else:
                vertical_path(tree[root][0], path)
                for j in tree[root][1:]:
                    vertical_path(j, [])
        
        vertical_path(root, [])
        
        print()



if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    
    
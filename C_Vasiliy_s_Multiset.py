class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, binNum):
        cur = self.root
        cur.count += 1
        for b in binNum:
            if b == "0":
                if not cur.left:
                    cur.left = TrieNode()
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TrieNode()
                cur = cur.right
            cur.count += 1

    def remove(self, binNum):
        cur = self.root
        cur.count -= 1
        for b in binNum:
            
            if cur.count == 0:
                cur.left = None
                cur.right = None
                break
            if b == "0":
                if cur.left.count == 1:
                    cur.left = None
                    break
                cur = cur.left
            else:
                if cur.right.count == 1:
                    cur.right = None
                    break
                cur = cur.right
            cur.count -= 1
    
    def search(self, binNum):
        cur = self.root
        ans = ""
        for b in binNum:
            if b == "0":
                if cur.right:
                    cur = cur.right
                    ans += "1"
                else:
                    cur = cur.left
                    ans += "0"
            else:
                if cur.left:
                    cur = cur.left
                    ans += "0"
                else:
                    cur = cur.right
                    ans += "1"
        return int(ans, 2)
    
n = int(input())
max_leng = len(bin(10 ** 9)) - 2
tr = Trie()
tr.insert("0" * max_leng)
for _ in range(n):
    si, num = input().split()
    num = int(num) 
    bin_rep = bin(num)[2:]
    bin_rep = "0" * (max_leng - len(bin_rep)) + bin_rep
    if si == "+":
        tr.insert(bin_rep)
    elif si == "-":
        tr.remove(bin_rep)
    else:
        b = tr.search(bin_rep)
        print(b ^ num)
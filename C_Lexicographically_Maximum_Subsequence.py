from collections import Counter
s = input()
count = Counter(s)

ind = 0
sub = ""
for k in sorted(count.keys())[::-1]:
    while count[k] > 0:
        sub += k
        count[k] -= 1
        while ind < len(s) and s[ind] != k:
            count[s[ind]] -= 1
            ind += 1
            
        ind += 1
        

print(sub)

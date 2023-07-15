a = input()
s = input()
arr_a = [int(num) for num in a]
arr_s = [int(num) for num in s]
arr_s.sort(reverse=True)

ind = 0
for num in arr_s:
    while ind < len(a) and num <= arr_a[ind]:
        ind += 1
    if ind <  len(a):
        arr_a[ind] = num
    else:
        break
res = ""
for num in arr_a:
    res += str(num)
print(res)


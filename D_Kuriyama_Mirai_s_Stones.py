n = int(input())
arr = list(map(int, input().split()))
m = int(input())
pref_sum_1 = [0]
new_arr = sorted(arr)
pref_sum_2 = [0]
for i in range(n):
    pref_sum_1.append(pref_sum_1[-1] + arr[i])
    pref_sum_2.append(pref_sum_2[-1] + new_arr[i])

for _ in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(pref_sum_1[r] - pref_sum_1[l - 1])
    else:
        print(pref_sum_2[r] - pref_sum_2[l - 1])
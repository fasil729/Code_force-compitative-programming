def make_prefix_sum(n):
    prefix_sum = [[0] * (n + 1) for _ in range(20)]
    for i in range(1, n + 1):
        for j in range(20):
            prefix_sum[j][i] = prefix_sum[j][i - 1] + ((i >> j) & 1)
    return prefix_sum


def solve(l, r, prefix_sum):
    mx = 0
    for i in range(20):
        mx = max(mx, prefix_sum[i][r] - prefix_sum[i][l - 1])
    
    num_unset_bits = r - l + 1 - mx
    return num_unset_bits


def main():
    t = int(input())
    prefix_sum = make_prefix_sum(2*10**5)
    for _ in range(t):
        l, r = map(int, input().split())
        result = solve(l, r, prefix_sum)
        print(result)


main()


# somehow working bu needs some modification
# t = int(input())
# for _ in range(t):
#     l, r = map(int, input().split())
#     c = r.bit_length()

#     # print("c", c)
#     mod = r % (2 ** (c - 1))
#     prev = 2 ** (c - 2)
#     n = r - l + 1
    
#     print(min(n - prev, n - mod - 1))
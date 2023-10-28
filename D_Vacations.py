n = int(input())
arr = list(map(int, input().split()))
memo = {}
def dp(contest, sport, index):
    if (contest, sport, index) in memo:
        return memo[(contest, sport, index)]
    if index >= n:
        return 0
    ans = 1 + dp(False, False, index + 1)
    if not contest and (arr[index] == 1 or arr[index] == 3):
        ans = min(ans, dp(True, False, index + 1))
    if not sport and (arr[index] == 2 or arr[index] == 3):
        ans = min(ans, dp(False, True, index + 1))
    if not contest and not sport and arr[index] == 3:
        ans = min(ans, dp(True, True, index + 1))
    memo[(contest, sport, index)] = ans
    return ans
print(dp(False, False, 0))
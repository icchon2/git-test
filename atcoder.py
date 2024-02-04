
n, d = map(int, input().split())
a = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n - 1):
    if abs(a[i + 1] - a[i]) > d:
        dp[i + 1] = dp[i]
    else:
        dp[i + 1] = dp[i] + 1    

print(dp[-1])        
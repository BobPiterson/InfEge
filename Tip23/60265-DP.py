dp = [0 for i in range(10000)]
dp[2] = 1

for i in range(100):
    if i != 11:
        dp[i + 1] += dp[i]
        dp[i * 2] += dp[i]
        dp[i * i] += dp[i]

print(dp[20])

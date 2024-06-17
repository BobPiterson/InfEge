dp = [0 for i in range(50)]
dp[2] = 1
for i in range(0, 23):
    dp[i + 1] += dp[i]
    dp[i * 2] += dp[i]

print(dp[22])

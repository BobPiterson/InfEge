dp = [[0 for j in range(7)] for i in range(26)]
dp[3][0] = 1

for i in range(4, 26):
    for j in range(7):
        if j == 0:
            if i % 2 != 0:
                dp[i][j] += dp[i - 1][j]
                dp[i][j] += dp[i - 3][j]
                if i - 5 >= 0:
                    dp[i][j] += dp[i - 5][j]
        else:
            u_j = 1 if i % 2 == 0 else 0
            dp[i][j] += dp[i - 1][j - u_j]
            dp[i][j] += dp[i - 3][j - u_j]
            if i - 5 >= 0:
                dp[i][j] += dp[i - 5][j - u_j]

print(dp[25][6])

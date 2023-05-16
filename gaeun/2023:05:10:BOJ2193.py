n = int(input())
dp = []
dp.append([0,1])
dp.append([1,1])
for i in range(2,n):
    total = dp[i-1][1]
    lastNum0 = dp[i-1][0]
    dp.append([total,total+lastNum0])
print(dp[n-1][1])

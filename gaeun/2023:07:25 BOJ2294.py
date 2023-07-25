import sys
readline = sys.stdin.readline
N,K = map(int,readline().split())
coinType = [0]*N
dp = [1e9]* (K+1)
for i in range(N):
    coinType[i] = int(readline())
dp[0] = 0
for n in range(1,K+1) :
    for i in range(N):
        value = n-coinType[i]
        if (value) >= 0 :
           dp[n] = min(dp[n],dp[value]+1)

if dp[K] == 1e9 :
    print(-1)
else :
    print(dp[K])
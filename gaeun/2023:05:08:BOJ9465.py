import sys
import copy
t = int(input())
answer = []

def getMax():
    n = int(input())
    dp = []
    for i in range(2) :
        line = list(map(int,input().split()))
        dp.append(line)
    result = copy.deepcopy(dp)
    for j in range(n):
        if j == 0 :
            result[0][j] = dp[0][j]
            result[1][j] = dp[1][j]
        else :
            
            # # 자신을 선택하지 않았을 때
            notSelf = max(result[0][j-1],result[1][j-1])
            #이전 대각선 값 + 자신
            pastMax0 = result[1][j-1]+result[0][j]
            pastMax1 = result[0][j-1]+result[1][j]
            twoPastMax0 = 0
            twoPastMax1 = 0
            if j >=2 :
                # 두번째 전 값 + 자신
                twoPastMax0 = max(dp[0][j-2],dp[1][j-2]) + dp[0][j]
                twoPastMax1 = max(dp[0][j-2],dp[1][j-2]) + dp[1][j]
            else :
                pastMax = 0
            result[0][j] = max(pastMax0,twoPastMax0)
            result[1][j] = max(pastMax1,twoPastMax1)
    return max(result[0][n-1],result[1][n-1])

for k in range(t):
    answer.append(str(getMax()))
print('\n'.join(answer))
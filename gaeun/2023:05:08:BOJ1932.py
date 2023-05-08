import copy
n = int(input())
dp = []
for i in range(n):
    line = list(map(int,input().split()))
    numList = copy.deepcopy(line)
    
    if i != 0 :
        for j in range(len(dp[i-1])):        
            line[j] = max(dp[i-1][j]+numList[j],line[j])
            line[j+1] = max(dp[i-1][j]+numList[j+1],line[j+1])
    dp.append(line)
    
print(max(dp[n-1]))
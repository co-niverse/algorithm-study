n = int(input())
nums = list(map(int,input().split()))
opt = list(map(int,input().split()))
minValue = int(1e9)
maxValue = int(-1e9)

def dfs(ind,status):
    global minValue,maxValue,opt
    if ind == n :
        minValue = min(minValue,status)
        maxValue = max(maxValue,status)
    else :
        # 더하기
        if opt[0] >0 :
            opt[0]-=1
            dfs(ind+1,status+nums[ind])
            opt[0]+=1
        # 뺄셈
        if opt[1] >0:
            opt[1]-=1
            dfs(ind+1,status-nums[ind])
            opt[1]+=1
        # 곱셈
        if opt[2]>0 :
            opt[2]-=1
            dfs(ind+1,status*nums[ind])
            opt[2]+=1
        # 나누기
        if opt[3]>0 :
            opt[3]-=1
            if status < 0 :
                dfs(ind+1,(abs(status)//nums[ind])*-1)   
            else :
                dfs(ind+1,status//nums[ind])
            opt[3]+=1


dfs(1,nums[0])
print(maxValue)
print(minValue)

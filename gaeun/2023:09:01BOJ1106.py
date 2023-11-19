import sys
readline = sys.stdin.readline
C,N = map(int,readline().rstrip().split())
city = [[] for i in range(N)]

maxPeople = -1
for n in range(N):
    cost,people = map(int,readline().rstrip().split())
    city[n]=[cost,people]
    maxPeople = max(maxPeople,people)

dp = [1e9 for i in range(C+maxPeople+1)]

for ind in range(1,len(dp)) :
    for cityInd in range(len(city)) :
        value = city[cityInd][1]
        needCost = city[cityInd][0]
        # 같을 때
        if value == ind :
            dp[ind] = min(dp[ind],needCost)
        # 배수로 나뉘어질 때
        elif (ind%value) == 0 :
            quotient = ind//value
            dp[ind] = min(dp[ind],needCost * quotient)
        # ind가 커서  이전 최소값에서 자신을 추가   
        elif value < ind :
            dp[ind] = min(dp[ind],dp[ind-value]+needCost)

result = 1e9
for r in range(C,C+maxPeople+1):
    result = min(result,dp[r])


print(result)
                    

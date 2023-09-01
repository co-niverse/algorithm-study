import sys
input = sys.stdin.readline

c, n = map(int, input().split())
cost_list = []

for i in range(n):
    cost, people = map(int, input().split())
    cost_list.append([cost, people])

dp = [1e7 for _ in range(c+100)] #최댓값이 100
dp[0] = 0

for cost, people in cost_list:
  for i in range(people, c+100):
    dp[i] = min(dp[i-people]+cost,dp[i])

print(min(dp[c:]))

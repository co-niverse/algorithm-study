## 1차 풀이 (시간 초과)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for i in range(n):
  coins.append(int(input()))

answer_list = [0] * (100001)
  
for i in coins:
  answer_list[i] = 1

for i in range(len(answer_list)):
  for j in coins:
    if answer_list[i] != 0 and i+j < (k+1):
      if answer_list[i+j] != 0:
        answer_list[i+j] = min(answer_list[i+j],answer_list[i] + 1)
      else:
        answer_list[i+j] = answer_list[i] + 1

if (answer_list[k] == 0):
  print(-1)
else:
  print(answer_list[k])


## 2차 풀이
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for i in range(n):
  coins.append(int(input()))

answer_list = [100001] * (k+1)
answer_list[0] = 0
  
for i in coins:
  for j in range(i, k+1): # 해당 동전 이후 부터
    answer_list[j] = min(answer_list[j],answer_list[j-i]+1)
    
if (answer_list[k] == 100001):
  print(-1)
else:
  print(answer_list[k])

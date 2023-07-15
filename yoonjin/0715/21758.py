### 1차 풀이
import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))

# 벌통, 1, 2 순서인 경우 -> 2는 맨 오른쪽임 / 1의 위치 구하기
max = -1e9
for i in range(1,n-1):
  # 2번 벌 입장
  total = sum(honey)-honey[n-1]-honey[i]
  # 1번 벌 입장
  total += sum(honey[:i-1])
  if max < total:
    max = total

# 1, 2, 벌통 순서인 경우 -> 1은 맨 왼쪽임 / 2의 위치 구하기
for i in range(1,n-1):
  # 1번 벌 입장
  total = sum(honey) - honey[i] - honey[n-1]
  # 2번 벌 입장
  total += sum(honey[i+1:])
  if max < total:
    max = total

# 1, 벌통, 2 순서인 경우
for i in range(1,n-1):
  total = sum(honey)-honey[0]-honey[n-1]+honey[i]
  if max < total:
    max = total

print(max)

###2차 풀이
import sys
input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))
total = sum(honey[:])
answer = 0
temp = honey[0]

# 1, 2, 벌통 순서인 경우 -> 1은 맨 왼쪽임 / 2의 위치 구하기
for i in range(1,n):
    temp += honey[i]
    answer = max(answer, total - honey[0] + total - temp - honey[i])

# 벌통, 1, 2 순서인 경우 -> 2는 맨 오른쪽임 / 1의 위치 구하기
honey.reverse()
temp = honey[0]
for i in range(1,n):
    temp += honey[i]
    answer = max(answer, (total - honey[0]) + (total - temp - honey[i]))

# 1, 벌통, 2 순서인 경우
for i in range(1,n):
    answer = max(answer, total - honey[0] - honey[-1] + honey[i])

print(answer)

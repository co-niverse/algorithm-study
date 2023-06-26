import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
robot = deque([0] * N) #로봇 있으면 1, 없으면 0
result = 0

while True:
  # 벨트, 로봇 한칸 회전
  A.rotate(1)
  robot.rotate(1)
  # 로봇 내려가는 부분 0
  robot[-1] = 0
  # 로봇 이동
  if robot:
    for i in range(N-2, -1, -1):
      if robot[i] == 1 and robot[i+1] == 0 and A[i+1] >= 1:
        robot[i+1] = 1
        robot[i] = 0
        A[i+1] -= 1
    robot[-1] = 0
  # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
  if robot[0] == 0 and A[0] >= 1:
    robot[0] = 1
    A[0] -= 1
  #내구도가 0인 칸의 개수가 k개 이상이면 종료
  if A.count(0) >= K:
    break
  result += 1

print(result)

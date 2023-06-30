import sys
input = sys.stdin.readline

# 입력 받기
h, w = map(int, input().split())
block = [[0]*w for _ in range(h)] # 블록이 없으면 0, 있으면 1, 빗물 고이면 2

# 블록을 채워보자
height = list(map(int, input().split()))

for i in range(w):
  for j in range(height[i]):
    block[j][i] = 1

# 탐색할 때 옆으로 쭉 갔을 때 블록이 있으면 고인물로 변경하기
def check(x,y):
  left_cnt = 0
  right_cnt = 0
  if block[x][y] == 0:
    # 양 옆으로 쭉 갔을 때 블록이 있는지 확인
    # 왼쪽으로 갔을 때
    for i in range(y):
      if block[x][i] == 1:
        left_cnt = 1
    # 오른쪽으로 갔을 때
    for i in range(y+1,w):
      if block[x][i] == 1:
        right_cnt = 1
    if left_cnt + right_cnt == 2:
      block[x][y] = 2

for i in range(h):
  for j in range(w):
    check(i,j)

answer = 0
for i in range(h):
  for j in range(w):
    if block[i][j] == 2:
      answer += 1

print(answer)

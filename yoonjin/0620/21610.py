##첫번째 풀이
from sys import stdin
n, m = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
move = [list(map(int, stdin.readline().split())) for _ in range(m)]

# 아래부터 시계 방향으로
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

# 대각선
ddx = [1,1,-1,-1]
ddy = [1,-1,1,-1]

#구름이 있는지 확인
clouds_exist = [[False]*n for _ in range(n)]

# 구름 좌표
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
move_cloud = []
for d,s in move:
  for i in range(len(clouds)):
    x = clouds[i][0] + dx[d-1]*s
    y = clouds[i][1] + dy[d-1]*s
    x %= n
    y %= n
    a[x][y] += 1
    clouds[i] = [x,y]
    clouds_exist[x][y] = True

  #구름 모두 사라짐
  clouds = []
  # 물복사버그
  count = 0
  for i in range(4):
    #경계를 넘지 않는 경우
    if(0 <= x+ddx[i] < n and 0 <= y+ddy[i] < n and a[x+ddx[i]][y+ddy[i]] >= 1):
        count += 1
    a[x][y] += count

  #물의 양이 2이상인 칸에 구름 생기고, 물의 양 2감소
  for i in range(n):
    for j in range(n):
      if (a[i][j] >= 2 and clouds_exist[i][j] == False):
        clouds.append([i,j])
        a[i][j] -= 2

result = 0
for i in range(n):
  for j in range(n):
    result += a[i][j]

print(result)



## 두번째 풀이
from sys import stdin
n, m = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
move = [list(map(int, stdin.readline().split())) for _ in range(m)]

# 아래부터 시계 방향으로
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

# 대각선
ddx = [1,1,-1,-1]
ddy = [1,-1,1,-1]

# 구름 좌표
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

for d,s in move:
  for i in range(len(clouds)):
    x = clouds[i][0] + dx[d-1]*s
    y = clouds[i][1] + dy[d-1]*s
    x %= n
    y %= n
    a[x][y] += 1
    clouds[i] = [x,y]
  
  # 물복사버그
  for x,y in clouds:
    for i in range(4):
      nx = x + ddx[i]
      ny = y + ddy[i]
      if 0<= nx < n and 0 <= ny < n:
        if a[nx][ny] != 0:
          a[x][y] += 1

    a[x][y] *= -1

  clouds.clear()

  #물의 양이 2이상인 칸에 구름 생기고, 물의 양 2감소
  for i in range(n):
    for j in range(n):
      if (a[i][j] >= 2):
        clouds.append([i,j])
        a[i][j] -= 2
      elif a[i][j] < 0:
        a[i][j] *= -1

result = 0
for i in range(n):
  for j in range(n):
    result += a[i][j]

print(result)

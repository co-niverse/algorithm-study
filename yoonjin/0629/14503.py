import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
visited = [[False]*m for _ in range(n)]
answer = 0
# 0, 3, 2, 1
# 북,서,남,동
# 북, 동, 남, 서
# 서, 북, 동, 남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 입력받기
r, c, d = map(int, input().split())

for _ in range(n):
    board.append(list(map(int, input().split())))

# 시작점 방문처리
visited[r][c] =True
answer += 1

while 1:
    flag = 0
    # 4방향 확인
    for i in range(4):
        # 왼쪽으로 회전
        d = (d+3) % 4
        nx = r + dx[d]
        ny = c + dy[d]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
          if visited[nx][ny] == False:
            visited[nx][ny] = True
            answer += 1
            r = nx
            c = ny
            flag = 1
            break
    # 4방향 모두 청소된 경우
    if flag == 0:
      #뒤쪽 칸이 벽이면 멈추기
      if board[r-dx[d]][c-dy[d]] == 1:
        break
      else:
        r = r - dx[d]
        c = c - dy[d]

print(answer)

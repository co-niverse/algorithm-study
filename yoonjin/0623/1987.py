#1차
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
answer = 0

def dfs(x, y, before):
    global answer
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 확인
        if (0 <= nx < r and 0 <= ny < c and board[nx][ny] not in before):
            dfs(nx, ny, before + board[nx][ny])
    if(len(before) > answer):
        answer = len(before)

dfs(0,0,board[0][0])

print(answer)

#2차
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(map(lambda x:ord(x)-65, input())) for _ in range(r)]
visited = [False] * 26
answer = 1
d = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[board[nx][ny]]:
                visited[board[nx][ny]] = True
                dfs(nx,ny,cnt+1)
                visited[board[nx][ny]] = False
                    
visited[board[0][0]] = True
DFS(0,0,answer)
print(answer)

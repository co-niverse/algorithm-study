from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

virus_combi=[0]*M #활성 바이러스를 담을 조합
result = 10000000

def comb(cur, cnt): #조합
    global result
    if(cnt==M): #조합이 완성되면
        result = min(result, bfs()) #작은 값을 갱신
        return
    for i in range(cur,len(v)):
        virus_combi[cnt]=i
        comb(i+1, cnt+1)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    visited = [[-1]*N for _ in range(N)] # 방문처리와 시간 계산 함께 진행
    for i in virus_combi: # 활성 바이러스 조합 queue에 담아주기
        queue.append([v[i][0],v[i][1]])
        visited[v[i][0]][v[i][1]] = 0 # 방문처리
   
    while queue:
        cx,cy = queue.popleft() # queue에서 위치 빼옴
        for d in range(4):
            nx = cx+dx[d]
            ny = cy+dy[d]
            if(nx<0 or ny<0 or nx>=N or ny>=N or visited[nx][ny]!=-1): # 범위 체크
                continue
            if(arr[nx][ny]==0 or arr[nx][ny]==2): # 빈칸이거나 비활성 바이러스이면
                queue.append([nx,ny]) # queue에 저장
                visited[nx][ny]=visited[cx][cy]+1 # 걸리 시간 증가
   
    time=0
    for i in range(N):
        for j in range(N):
            if(arr[i][j]==0): # 빈칸인데
                if(visited[i][j]==-1): # 방문을 하지 않았다면 (모든 빈칸을 방문하지 못함)
                    return 10000000 # 큰 값 return
                time=max(time,visited[i][j]) # 방문을 했다면 시간 최대값으로 변경
    return time #걸린시간



v = [] #바이러스 위치를 담아줄 배열
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2: # 바이러스라면
            v.append([i,j]) # 위치 저장

comb(0,0) # 조합 진행

if result==10000000: #모든 빈칸을 방문하지 못했다면
    result = -1

print(result)

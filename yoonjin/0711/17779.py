import sys
input = sys.stdin.readline
n = int(input())
A = []

for i in range(n):
    A.append(list(map(int, input().split())))

def calculate(r,c,d1,d2):
    board = [[0]*(n+1) for i in range(n+1)]
    # 5번 선거구
    ## 경계선
    for i in range(d1+1):
      # 1
      board[r+i][c-i] = 5
      # 4
      board[r+d2+i][c+d2-i] = 5
    for i in range(d2+1):
      # 2
      board[r+i][c+i] = 5
      # 3
      board[r+d1+i][c-d1+i] = 5
    ## 경계선 내부
    for i in range(r+1, r+d1+d2):
        flag = False
        for j in range(1, n+1):
          if board[i][j] == 5:
              flag = not flag
          if flag:
              board[i][j] = 5
        
    for x in range(1,n+1):
      for y in range(1,n+1):
        if x < r+d1 and y <= c and board[x][y] == 0:
            board[x][y] = 1
        elif x <= r + d2 and c < y and board[x][y] == 0:
            board[x][y] = 2
        elif r+d1 <= x and y < c-d1+d2 and board[x][y] == 0:
            board[x][y] = 3
        elif r+d2 < x and c-d1+d2 <= y and board[x][y] == 0:
            board[x][y] = 4

    ## 인구 계산
    count = [0 for i in range(5)]
    for i in range(1,n+1):
      for j in range(1,n+1):
          count[board[i][j]-1] += A[i-1][j-1]
    # 인구 차이
    sub = max(count) - min(count)
    return sub
  

minSub = 1e9
for r in range(1,n+1):
  for c in range(1,n+1):
    for d1 in range(1,n+1):
      for d2 in range(1,n+1):
        # d1, d2 조건 구하기
        if (1 <= r < r+d1+d2 <= n) and (1 <= c - d1 < c < c +d2<= n):
            calSub = calculate(r,c,d1,d2)
            if(calSub < minSub):
                minSub = calSub

print(minSub)

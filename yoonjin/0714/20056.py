### 1차 풀이
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
fireballs =[]
for _ in range(m):
    r,c,m,s,d = list(map(int, input().split()))
    fireballs.append([r-1,c-1,m,s,d])

board = [[[] for _ in range(n)] for _ in range(n)]

# 방향
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

for _ in range(k):
  # 파이어볼 이동
  for r,c,m,s,d in fireballs:
    nr = (r + s*dx[d]) % n #1-n번 행 연결되어 있으니까 % n
    nc = (c + s*dy[d]) % n
    board[nr][nc].append((m,s,d)) # r,c 위치에 m,s,d 저장
  # 이동 끝난 후, 2개 이상의 파이어볼이 있는지 확인
  for r in range(n):
    for c in range(n):
      # 2개 이상인 경우
      if len(board[r][c]) >= 2:
            # 변수 설정
            sum_m = 0 # 질량
            sum_s = 0 # 속력
            isEven = 0 # 짝수
            isOdd = 0 # 홀수
            # 한 칸에 있던 파이어볼의 성질 파악
            for (m,s,d) in board[r][c]:
                sum_m += m
                sum_s += s
                if d % 2 == 0:
                    isEven += 1
                else:
                    isOdd += 1
            # 원래 있던거 없애고, 4개로 나누기
            # 방향
            if(isEven == len(board[r][c]) or (isOdd == len(board[r][c]))):
                nd = [0,2,4,6]
            else:
                nd = [1,3,5,7]
            if sum_m//5:
              for d in nd:
                  fireballs.append([r,c,sum_m//5,sum_s//(len(board[r][c]))])
            # 원래꺼 없애기
            board[r][c].clear()
      if len(board[r][c]) == 1:
        for m,s,d in board[r][c]:
          fireballs.append([r,c,m,s,d])
        board[r][c].clear()

answer = 0
print(fireballs)
for i in fireballs:
  answer += i[2]

print(answer)

### 2차 풀이
import sys
input = sys.stdin.readline

n, m, k= map(int, input().split())
fireballs = []
for _ in range(m):
    r,c,m,s,d = list(map(int, input().split()))
    fireballs.append([r-1,c-1,m,s,d])

board = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    # 파이어볼 이동
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        nr = (cr + cs * dx[cd]) % n  # 1-n 연결되어 있으니까 % n 수행 
        nc = (cc + cs * dy[cd]) % n
        board[nr][nc].append([cm, cs, cd])

    # 2개 이상인지 체크
    for r in range(n):
        for c in range(n):
            # 2개 이상인 경우
            if len(board[r][c]) > 1:
                sum_m = 0 # 질량 합
                sum_s = 0 # 속도 합
                isOdd = 0 # 홀수 개수 계산
                isEven = 0 # 짝수 개수 계산
                length = len(board[r][c])
                while board[r][c]:
                    _m, _s, _d = board[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        isOdd += 1
                    else:
                        isEven += 1
                if isOdd == length or isEven == length:  # 모두 홀수이거나 모두 짝수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m//5:  # 질량 0이면 없어짐
                    for d in nd:
                        fireballs.append([r, c, sum_m//5, sum_s//length, d])

            # 1개인 경우
            if len(board[r][c]) == 1:
                fireballs.append([r, c] + board[r][c].pop())

print(sum([f[2] for f in fireballs]))

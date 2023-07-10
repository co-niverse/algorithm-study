import sys
input = sys.stdin.readline

# 입력받기
dice = list(map(int, input().split()))
# 파란색 칸에서 시작하는 경우에만 파란색 화살표
# 각 위치마다 이동할 수 있는 다음 칸의 위치
graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]
# 각 위치마다 점수
score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]
# 정답
answer = 0

def backtracking(depth, result, horses):
  global answer
  # 게임은 10개의 턴으로 진행
  if depth == 10:
    answer = max(answer, result)
    return

  # 말의 개수는 4개
  for i in range(4):
    # 현재 말의 위치
    x = horses[i]
    # 현재 말이 파란색에 있는지 확인
    if len(graph[x]) == 2:
      # 파란색 화살표 따라서 이동
      x = graph[x][1]
    else:
      # 빨간색 화살표 따라서 이동
      x = graph[x][0]

    # 주사위 값 만큼 말 이동하기
    # 위에서 처음 한번 이동했으니까 1부터 시작
    for j in range(1,dice[depth]):
        x = graph[x][0]

    # 도착했거나, 도착하지 않았는데 말이 없다면
    if x==32 or (x < 32 and x not in horses):
        # 이전 말의 위치
        before = horses[i]
        # 현재 말의 위치
        horses[i] = x
        backtracking(depth+1, result+score[x],horses)
        horses[i] = before

backtracking(0,0,[0,0,0,0])
print(answer)

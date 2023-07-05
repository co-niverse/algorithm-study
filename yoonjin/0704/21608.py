import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
fav = []
board = [[0] * n for _ in range(n)]

for i in range(n*n):
  fav.append(list(map(int, input().split())))

# 인접한 칸 = 동서남북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


for student_list in fav:
  student_num = student_list[0]
  # 좋아하는 학생은 student_list[1] ~ student_list[4]
  # board 순회하기
  for i in range(n):
    for j in range(n):
      # 1. 비어 있는 칸 중에서
      if board[i][j] == 0:
        # 1. 인접한 칸에 좋아하는 학생이 있는지 개수 확인
        fav_num_list = [] # 동서남북 순서로 좋아하는 학생 수 저장
        for k in range(4):
          fav_num = 0
          nx = i+dx[k]
          ny = j+dy[k]
          # 좋아하는 학생이 있는지 확인
          if board[nx][ny] in student_list[1:]:
            fav_num += 1
            fav_num_list[k].append(fav_num)
        # 1. 인접한 칸에서 가장 많은 칸이 하나만 있으면 자리 정함
        if len(fav_num_list) == len(set(fav_num_list)):
          # 1. 가장 많은 칸 인덱스 뽑기
          max = 0
          max_index = -1
          for l in range(4):
            if max < fav_num_list[l]:
              max = fav_num_list[l]
              max_index = l
          # 1. 자리 정하기
          board[i+dx[max_index]][j+dy[max_index]] = student_num
        # 2. 인접한 칸에서 가장 많은 칸이 여러개이면
        else:
          # fav_num_list 중에서 최댓값을 가진 애들끼리 자신의 인접한 칸 중에서 비어있는 칸의 개수를 구해서 저장한다.
          # fav_num_list에서 최댓값 가진 애들의 index 구하기
          m = max(fav_num_list)
          fav_num_list_index = [index for index,v in enumerate(fav_num_list) if v == m]
          empty_num_list = []
          for ind in fav_num_list_index:
            # i, j에서 fav_num_list_index가 0,1,2,3 순서로 dx, dy 더한게 새로운 좌표, 여기에다가 또 인접한 것들 중 비어 있는 칸 구하기
            ix = i+ dx[ind]
            iy = i +dy[ind]
            # (ix, iy)에 대해서 인접한 칸들 구하기
            empty_num = 0
            for a in range(4):
              ax = ix + dx[a]
              ay = iy + dy[a]
              # 비어 있는 칸 구하기
              if board[ax][ay] == 0:
                empty_num += 1
            empty_num_list[a].append(empty_num)
          # empty_num_list에서 max가 있으면 
          if len(empty_num_list) == len(set(empty_num_list)):
            board[i+dx[max_index]][j+dy[max_index]] = student_num

          
# 학생의 만족도 합 구하기

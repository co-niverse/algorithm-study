import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

volume = [[0] * (M+1) for _ in range(N+1)]

# 시작점 넣기
volume[0][S] = 1

# 가능한 곳 1로 채우기
for i in range(N):
  for j in range(M+1):
    # 1인 곳 찾아서 다음 연산 수행하기
    if volume[i][j] == 1:
        num = j
        # V로 더하기 빼기 실시
        up_volume = num + V[i]
        down_volume = num - V[i]
        # 0이상 M이하이면 다음 volume 칸 1로 바꾸기
        if(0 <= up_volume <= M):
            volume[i+1][up_volume] = 1
        if(0 <= down_volume <= M):
            volume[i+1][down_volume] = 1

#  마지막 줄 확인
end = []
for i in range(M+1):
  if volume[N][i] == 1:
    end.append(i)

if len(end) == 0:
    print(-1)
else:
    print(max(end))
